######################################################################
# Classifier for good and bad deals and its evaluation               #
# Author: Himanshu Verma                                             #
# Date: 03/28/2014                                                   #
######################################################################

#!/usr/apps/Python/bin/python
################ import basic libraries #################

from RetailMeNotHeader import *
from RetailMeNotFunctions import *

stopWords = open('data/stop_words.txt', 'r').read().split()
badDeals = open('data/RetailMeNotBadDeals.txt','r') ## file handle to read BadDeals.txt ##
goodDeals = open('data/RetailMeNotGoodDeals.txt','r') ## file handle to read GoodDeals.txt ##
testDeals = open('data/RetailMeNotTestDeals.txt','r') ## file handle to read TestDeals.txt ##
testFileOutput = open('output/RetailMeNotOutputFile.txt', 'w') ## Ouput file with classified deals ##

allDeals = open('data/RetailMeNotDeals.txt','r')
allDealList=[]
goodDealList=[]
badDealList=[]
allTopics=[]
badTrainingDeals =[]
goodTrainingDeals=[]
trainingDeals=[]
dealsKeyWords = ['off','offer','deal','save','free','sale','clearance','coupon','code'] ## keyword list for feature extraction ##
dealsKeyWords = [stem(x) for x in dealsKeyWords]## stemming ##
for line in goodDeals:
    goodDealList.append(line)
for line in allDeals:
    allDealList.append(line)

for line in badDeals:
    badDealList.append(line)

### Finding important words contributing to the most probable topic(Group) ################
#fullText=[stopwords_remove(document,stopWords) for document in goodDealList]
fullText=[stopwords_remove(document,stopWords) for document in allDealList]
dictionary = corpora.Dictionary(fullText)
corpus = [dictionary.doc2bow(text) for text in fullText]
tfidf = models.TfidfModel(corpus) 
corpusTfidf = tfidf[corpus]
numberOfTopics = 2
lda = models.LdaModel(corpusTfidf, id2word=dictionary, num_topics=numberOfTopics)

for i in range(0, numberOfTopics):
    temp = lda.show_topic(i, 50)## we choose top 10 words this time ##
    terms = []
    for term in temp:
        terms.append(term[1])
    allTopics.append(terms)
#   print "terms for topic " + str(i) +  '  '+ ", ".join(terms) ### for debugging
  

maximumProbableTopic = allTopics[max(lda[corpus[1]],key=itemgetter(1))[0]] ## most probable topic's keywords are also considered as features##
maximumProbableTopic = [stem(x) for x in maximumProbableTopic]
dealsKeyWords = set(dealsKeyWords + maximumProbableTopic)## making set to have unique keywords ##

## arranging data for training ##
for line in badDealList:
    line = stopwords_remove(re.sub(r"(\.+){2,}|([\.][\s])|(\.$)", " ", line.rstrip('\n')), stopWords)
    temp = (line,'bad')
    badTrainingDeals.append(temp)

for line in goodDealList:
    line = stopwords_remove(re.sub(r"([\.][\s])|(\.$)", " ", line.rstrip('\n')),stopWords)
    temp = (line,'good')
    goodTrainingDeals.append(temp)

## we used naive bayesian classifier for classification ####
trainingDeals = badTrainingDeals + goodTrainingDeals
random.shuffle(trainingDeals)
featureset = [(newFeatureSet(a,dealsKeyWords,stopWords), b) for (a,b) in trainingDeals] ## feature extraction ##
classifier = nltk.NaiveBayesClassifier.train(featureset) ## training ##

## classifying test data and writing output to the file ##
for line in testDeals:
    line1 = stopwords_remove(re.sub(r"([\.][\s])|(\.$)", " ", line.rstrip('\n')),stopWords)
    y=classifier.classify(newFeatureSet(line1,dealsKeyWords,stopWords))
    testFileOutput.write(line.rstrip('\n') + '   ' +y+'\n')

testFileOutput.close()

#########  Classifier Evaluation (ACCURACY And PRECISION And RECALL And F-TEST ###################
featureset = [(newFeatureSet(a,dealsKeyWords,stopWords), b) for (a,b) in trainingDeals]
train_set, test_set = featureset[:30], featureset[20:]

classifier2 = nltk.NaiveBayesClassifier.train(train_set)
print "Accuracy : ", nltk.classify.accuracy(classifier2, test_set)
classifier2.show_most_informative_features(4)
referenceSets = collections.defaultdict(set)
testSets = collections.defaultdict(set)

for i, (fea, label) in enumerate(test_set):
    referenceSets[label].add(i)
    observed = classifier2.classify(fea)
    testSets[observed].add(i)

print 'good precision:', nltk.metrics.precision(referenceSets['good'], testSets['good'])
print 'good recall:', nltk.metrics.recall(referenceSets['good'], testSets['good'])
print 'good F-measure:', nltk.metrics.f_measure(referenceSets['good'], testSets['good'])
print 'bad precision:', nltk.metrics.precision(referenceSets['bad'], testSets['bad'])
print 'bad recall:', nltk.metrics.recall(referenceSets['bad'], testSets['bad'])
print 'bad F-measure:', nltk.metrics.f_measure(referenceSets['bad'], testSets['bad'])
