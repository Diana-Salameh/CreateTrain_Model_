#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier


# In[9]:


def red_csv():
    # read dataframe
    train = pd.read_csv("C:\\Users\\King\\Desktop\\project_\\train.txt", header=None, sep=" ")
    #read all columns and rows
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    return train


# In[10]:


#delete ":" of data
def extract_query(qstr):
    return qstr[4:]

def extract_features(features):
    return features.split(':')[1]


# In[11]:


def df_preparing(df):
    df[1] = df[1].apply(extract_query)
    df[df.columns[2:]] = df[df.columns[2:]].applymap(extract_features)
    return df


# In[23]:


def build_model():
    train_df = df_preparing(red_csv())
    # Divide the data into training and testing
    test=train_df[0:300]
    train=train_df[300:]
    
    # Divide the train data into x, y
    train_X = train[train.columns[2:]]
    train_y = train[0]
    
    # Divide the test data into x, y
    test_X = test[test.columns[2:]]
    test_x=test_X[test_X.columns[2:]][:296:4]
    test_y= test[0]    
     
    clf = KNeighborsClassifier()
    # Data training
    clf.fit(train_X, train_y)
    # checked of score
    clf.score(train_X,train_y)

    # Test model
    distances, indices = clf.kneighbors(test_X,  n_neighbors=10)
    return distances,indices


# In[28]:


def main():
    # build array 
    
    
    distances,indices=build_model()
    
    # print prediction
    pd.DataFrame(distances)
    pd.DataFrame(indices)


# In[29]:


if __name__ == "__main__":
    main()


# In[ ]:




