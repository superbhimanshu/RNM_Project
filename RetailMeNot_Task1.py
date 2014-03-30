######################################################################
# Read data file and analyze Freq                                    #
# Author: Himanshu Verma                                             #
# Date: 03/24/2014
######################################################################

## Import header file and functions library ##
from RetailMeNotHeader import *
from RetailMeNotFunctions import *

## stopWords : List of non informative words ##
stopWords = open('data/stop_words.txt', 'r').read().split()
textFile = open('data/RetailMeNotDeals.txt', 'r') ## Deals.txt##
wordList =[] ##maintain an all words list for frequency distribution analysis
typeOfGuitar=set() ## maintains a type unique guitar type ##


for line in textFile:
    line = stopwords_remove(re.sub(r"(\.+){2,}|([\.][\s])|(\.$)", " ", line.rstrip('\n')), stopWords)
    tempWordList=[]
    for word in line:
        if((word=='$') or (word=='%') or (len(wn.synsets(word))!=0)
                                          or (re.search(r'(.\.[a-zA-Z][a-zA-Z])' , word) !=None)):
            tempWordList.append(word)
    wordList = wordList + tempWordList
    if "guitar" in line:
        GuitarType = findTypeGuitar(line)
        if GuitarType != '':
            typeOfGuitar.add(GuitarType)


print typeOfGuitar
freqdist2 = FreqDist(wordList) ## Frequency distribution of words across the deals ##
freqdist2 .plot (40, cumulative =False)
sorted_fredist  = sorted(freqdist2.iteritems(), key=operator.itemgetter(1))
f= open('RMN_WORD_FREQ_DATA.txt','w')
i=0
while(i!=len(sorted_fredist)):
    f.write(str(sorted_fredist[i][0]) + ", " + str(sorted_fredist[i][1]) + "\n")
    i=i+1

f.close()
