# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 23:33:52 2019

@author: Shreshto
"""

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

cv1 = CountVectorizer(stop_words)
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