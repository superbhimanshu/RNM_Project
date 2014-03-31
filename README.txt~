FILES DESCRIPTION:-

------------------Data File---------------
1. RetailMeNotDeals.txt - has same data as in Deals.txt
2. RetailMeNotBadDeals.txt - BadDeals data for training classifier
3. RetailMeNotGoodDeals.txt - GoodDeals data for training classifier
4. RetailMeNotTestDeals.txt - Test data for classification

------------------Code Files--------------
1. RetailMeNotHeader.py - All required imports are mentioned in this file
2. RetailMeNotFunctions.py - This is the function library
3. test_RetailMeNotFunctions.py - This file can be used for testing, It has testing scenarios for the functions 
(using py.test filename command) 
4. RetailMeNot_Task1.py - Solution to Task1 has been implemented in this file
ANSWERS:-
-Words Frequency Distribution has been implemented- RetailMeNotWordsDistribution.png shows the most frequent 
terms used accross all the deals.
Ascending order of word frequency distribution has been saved in RetailMeNotWordsDistributionData.txt to access lowest frequent terms and 
for further processing. This file can also be used for implementing caching for faster analysis when new data comes. 

5. RetailMeNot_Task2.py- Topic modeling using LDA technique has been done in this file as per requirements of 
Task2
6. RetailMeNot_Task3.py - Implemented classification algorithm using naive bayesian classifier, feature extractor with four defined features(length of data, $ sign is present or not, % sign is present or not, keyword present or not) and classifier evaluator(Precision, Recall and F-Test).
ANSWERS:-
Accuracy :  0.8
Most Informative Features
                $Present = True             good : bad    =      2.6 : 1.0
                %Present = True             good : bad    =      2.6 : 1.0
                 keyword = True             good : bad    =      2.4 : 1.0
                 keyword = False             bad : good   =      1.6 : 1.0
good precision: 0.875
good recall: 0.7
good F-measure: 0.777777777778
bad precision: 0.75
bad recall: 0.9
bad F-measure: 0.818181818182

Our classifier is not very general because we used feature extractor specific to short text and features related to deals only. 
It will need more tuning if data form changes to long texts as more features can be extracted because of extra information.
Classification can surely be improved by increasing the amount of training data. Moreover, if we can increase the number of 
relevant features it will surely enhance the performance.
Word Sense Disambiguation can be implemented to find the proper context of each word present in the data and we can  
estimate the closeness of the words with keywords like "deals", "offer" and "percentage off" etc.



