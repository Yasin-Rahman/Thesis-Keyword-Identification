# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 21:06:37 2018

@author: Shreshto
"""

#Importing modules
#Importing modules
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB,GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.feature_extraction import text



"""#For online import
import io
import requests
url="https://raw.githubusercontent.com/Yasin-Rahman/CSV/master/2015.csv"
s=requests.get(url).content
dataset=pd.read_csv(io.StringIO(s.decode('utf-8')))
dataset = pd.read_csv(url)"""

#read CSV file
df=pd.read_csv('Comment.csv',sep=',',names=['Status','Message'],encoding ="utf-8")

#Visual representation of raw data
print("Visual of Raw dataset head")
print(df.head())

#Statistics of data
print("Length of the dataframe: ",len(df))
print("No. of Spam message: ",len(df[df.Status=='spam']))
print("No. of Ham message: ",len(df[df.Status=='ham']))

#Assigning numeric value to spam and ham keyword
df.loc[df["Status"]=='ham',"Status",]=1
df.loc[df["Status"]=='spam',"Status",]=0

#Show updated dataframe
print("Dataset with updated column name")
print(df.head())

#diving the data between dependent & indeendent variables
df_x=df["Message"]
df_y=df["Status"]

#Diving total data into rain and test set
#the ration of train and test data is about 6:4
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2, random_state=4)


#Adding bangla stop words
stop_words = [str(x.strip()) for x in open('stopwords.txt','r',encoding="utf-8").read().split('\n')]

print("Stop words Used: ",stop_words)

cv1 = CountVectorizer(stop_words = stop_words)
#fitting the training data with CountVectorizer
x_traincv=cv1.fit_transform(x_train)
#New array for GaussianB
x_dense = x_traincv.todense()

#Key Words first 200
sum_words = x_traincv.sum(axis=0) 
words_freq = [(word, sum_words[0, idx]) for word, idx in     cv1.vocabulary_.items()]
words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
#Print top 200 Most Common Spam words
print('The Top 200 Keywords Are:')
print(words_freq[:200])


#converting training data to array
a=x_traincv.toarray()

#Showing array representation of first data
print("First item of the converted array")
print(a[0])

#Showing the occurance of words in first item
print("Occurance of words in first line")
cv1.inverse_transform(a[0])

#Showing the actual data
print("First actual data")
x_train.iloc[0]

#Setting up testing data
x_testcv=cv1.transform(x_test)
x_testcv.toarray()
#New Array for GaussianB
x_densetest = x_testcv.todense()

#Using Multinomial Naive Bayesian formula for machine learning
mnb = MultinomialNB()
gnb = GaussianNB()
bnb = BernoulliNB()

#Setting training data as integer
y_train=y_train.astype('int')


#Fitting traing data
y_train
mnb.fit(x_traincv,y_train)

GaussianNB(priors=None)
gnb.fit(x_dense,y_train)

bnb.fit(x_traincv,y_train)



#Storing a data item
print("First data item of test set")
testmessage=x_test.iloc[0]
print(testmessage)

#Calculating and showing predicted result
predictions=mnb.predict(x_testcv)
print("Predicted array by MultinomialB")
print(predictions)

predictions_g=gnb.predict(x_densetest)
print("Predicted array by GaussianB")
print(predictions_g)


predictions_b=bnb.predict(x_testcv)
print("Predicted array by BernoulliB")
print(predictions_b)


#Showing the actual result
a=np.array(y_test)
print("Actual Test Array data")
print(a)

#Counting No. of correct predictions
count=0
for i in range (len(predictions)):
    if predictions[i]==a[i]:
        count=count+1
print("No. of Correct predictions: ",count)

count_g=0
for i in range (len(predictions_g)):
    if predictions_g[i]==a[i]:
        count_g=count_g+1
print("No. of Correct predictions: ",count_g)

count_b=0
for i in range (len(predictions_b)):
    if predictions_b[i]==a[i]:
        count_b=count_b+1
print("No. of Correct predictions: ",count_b)


#Calculating accuracy
print("No. of observations: ",len(predictions))
acc = (count/len(predictions))*100
print("The accuracy is(MultinomialB): ",acc,"%")

print("No. of observations: ",len(predictions_g))
acc = (count_g/len(predictions_g))*100
print("The accuracy is(Gaussian): ",acc,"%")

print("No. of observations: ",len(predictions_b))
acc = (count_b/len(predictions_b))*100
print("The accuracy is(BernoulliB): ",acc,"%")



