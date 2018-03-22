import csv
#import os.path
import pandas as pd
from collections import defaultdict
count = 0
count1= 0 
sum1=0

with open('dfp.csv') as csvfile:
    reader = csv.reader(csvfile)
    
    data = []
    for row in reader:
        data.append(row)
    abc = []   
    data1=[] 
    primary = []
    for i in range(1,len(data)):
        data1.append(data[i][2:])
    
    for i in range(0,len(data1)):
        for j in range(0,len(data1[i])):
            #print(data1[i][j])
            if data1[i][j]=='1':
                for k in range(0,len(data1)):
                    if data1[k][j]=='0' and i!=k:
                        count = count + 1
                    sum1 = sum1 + int(data1[k][j])    
                if count==148:
                    count1 = count1+1    
                    
            else:
                for k in range(0,len(data1)):
                    sum1 = sum1 + int(data1[k][j])  
                    
            if sum1 == 1 and j not in primary:
                primary.append(j)
            sum1=0  
        if count1>0:
            abc.append(i)
            
        count=0
        count1=0   
   
with open('tertiary.csv','w') as csvfile:
    writer = csv.writer(csvfile)    
   
    for j in primary:
        for i in range(1,len(data)):  
            key = data[0][j+2]
            key1 = data[i][1]
            if data[i][j+2] == '1':
                writer.writerow([key1,key])

columns = ['Source','Target']
data2 = pd.read_csv("tertiary.csv",names=columns, encoding ="ISO-8859-1")
            
df = pd.DataFrame(data2)
df_1 = pd.get_dummies(df.Target)

#print(df_1.head())
#print(df.head())

df_s = df['Source']
df_pivoted = pd.concat([df_s,df_1], axis=1)
df_pivoted.drop_duplicates(keep='first',inplace=True)
#print(df_pivoted[:5])

#print(len(df_pivoted))

cols = df_pivoted.columns

cols = cols[1:]


df_pivoted = df_pivoted.groupby('Source').sum()
df_pivoted = df_pivoted.reset_index()

#print(df_pivoted[:5])

#print(len(df_pivoted))

def printf(x1,x2):
    print(x1,x2)

df_pivoted.to_csv("tertiary_pivoted1.csv")
x = df_pivoted[cols]
y = df_pivoted['Source']


import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import train_test_split
import numpy as np

mnb_tot = MultinomialNB()
mnb_tot = mnb_tot.fit(x, y)

with open('tertiary_pivoted1.csv') as csvfile:
    reader = csv.reader(csvfile)
    data = []
    for row in reader:
        data.append(row)    

test=[0]*115

def tertiary(p1):
    for i in range(0,len(p1)):
        for j in range(2,117):
            if(p1[i]==data[0][j]):
                test[j-2]=1
    disease_pred = mnb_tot.predict(test)
    if sum(test)>0:
        return printf('Disease after tertiary classification: ', disease_pred)
    
