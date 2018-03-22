import pandas as pd
from sklearn import tree
from sklearn.datasets import load_iris
import numpy as np
import pydotplus
from IPython.display import Image
import csv

with open('secondary_pivoted2 (classified).csv') as csvfile:
    reader = csv.reader(csvfile)
    
    data = []
    for row in reader:
        data.append(row)    

def printf(x1,x2):
    print(x1,x2)
index=[]
columns=data[0][2:]

df_ = pd.DataFrame(index=index, columns=columns)
df_ = df_.fillna(0)

def search(test1):
    y=0
    m=0
    z=0
    for k in range(0,len(test1)):
        if test1[k]==1:
            z=z+1
    for j in range(0,len(dataset)):
        for i in range(0,len(test1)):
            if test1[i]==1 and dataset[j,i]==1:
                y=y+1
        if y==z:
            m=m+1
            df_.loc[m]=dataset[j,:]
        y=0
    
    if len(df_)>0:        
        return printf(df_,'')      
    else:
        return printf('No disease found; Kindly provide different symptoms','')

dataframe = pd.read_csv("test_secondary.csv", header=None)
dataset = dataframe.values
iris=load_iris()

def convert_output(dataset):
    #function to convert output column(last) to numerical number
    names=list(set(dataset[:,-1]))
    for i in range(len(dataset)):
        dataset[i,-1]=names.index(dataset[i,-1])
    return dataset,names





test1=[0]*234

def secondary(p1):    
    for i in range(0,len(p1)):
        for j in range(2,236):
            if(p1[i]==data[0][j]):
                test1[j-2]=1

    if sum(test1)>0:            
        search(test1)  
        dataset1=df_.values
    #dataset,names=convert_output(dataset)
    #dataset=dataset.astype('int')
    if len(df_)>0:
        dtc=tree.DecisionTreeClassifier(criterion="entropy")
        dtc.fit(dataset1[:,0:-1].astype(int),dataset1[:,-1])    
        dot_data = tree.export_graphviz(dtc, out_file=None) 
        graph = pydotplus.graph_from_dot_data(dot_data) 
        graph.write_pdf("iris2.pdf") 
        return printf('Disease after secondary classification: ', dtc.predict(test1))
'''
with open("iris.dot", 'w') as f:
    f = tree.export_graphviz(dtc, out_file=f)'''


'''
dot_data = tree.export_graphviz(dtc, out_file=None, 
                         feature_names=[str(i) for i in range(len(dataset[:,0:-1]))],  
                         class_names=[str(i) for i in range(len(dataset[:,-1]))],  
                         filled=True, rounded=True,  
                         special_characters=True)  
graph = pydotplus.graph_from_dot_data(dot_data)  
Image(graph.create_png())'''
