######################################################################
# Read data file and analyze Freq                                    #
# Author: Himanshu Verma                                             #
# Date: 03/24/2014
######################################################################

## Import header file and functions library ##
from RetailMeNotHeader import *
from RetailMeNotFunctions import *

## stopWords : List of non informative words ##
stopWords = open('stop_words.txt', 'r').read().split()
textFile = open("RetailMeNotDeals.txt", "r") ## Deals.txt##
wordList =[]
typeOfGuitar=set() ## maintains a type unique guitar type ##


for line in textFile:
    line = stopwords_remove(re.sub(r"(\.+){2,}|([\.][\s])|(\.$)", " ", line.rstrip('\n')), stopWords)
    wordList = wordList + line
    if "guitar" in line:
        GuitarType = findTypeGuitar(line)
        if GuitarType != '':
            typeOfGuitar.add(GuitarType)


print typeOfGuitar
freqdist2 = FreqDist(wordList) ## Frequency distribution of words across the deals ##
freqdist2 .plot (40, cumulative =False)
sorted_fredist  = sorted(freqdist2.iteritems(), key=operator.itemgetter(1))
