#!/usr/bin/env python
# coding: utf-8

# In[89]:


#!pip install xgboost
import pandas as pd
import numpy as np
from itertools import islice 
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.linear_model import Ridge
import math
import xgboost as xgb


# In[90]:


def red_csv():
    # read dataframe
    train = pd.read_csv("C:\\Users\\King\\Desktop\\project_\\train.txt", header=None, sep=" ")
    #read all columns and rows
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    return train


# In[91]:


#delete ":" of data
def extract_query(qstr):
    return qstr[4:]
def extract_features(features):
    return features.split(':')[1]


# In[92]:


def df_preparing(df):
    df[1] = df[1].apply(extract_query)
    df[df.columns[2:66]] = df[df.columns[2:66]].applymap(extract_features)
    return df


# In[93]:


#call of  function
train_df = df_preparing(red_csv())


# In[94]:


# Divide the four ranks
# belonging to the same person into 1d 
# matrix and group all persons 
# together in a two-dimensional matrix  
def convert(lst, var_lst): 
    it = iter(lst) 
    return [list(islice(it, i)) for i in var_lst] 
def build_train_y():
    # Take col 0 
    train_y = train_df[train_df.columns[0]]
    # biuld 2d Array
    var_lst2 = [4 for i in range(0,204)] 
    train_y=convert(train_y[:816], var_lst2)
    return train_y


# In[95]:


# Divide the data into training and testing
def Divide_data():
    # Take rows from 0 to 816
    train_x=train_df[train_df.columns[2:]][:816:4]
    # Take rows from 816 to end
    test=train_df[train_df.columns[2:]][816::4]
    return train_x,test


# # Create models

# In[96]:


def build_modele_one():
    train_x,test=Divide_data()
    train_y=build_train_y()
    model_one = MultiOutputRegressor(GradientBoostingRegressor(random_state=0))
    # Data training
    model_one.fit(train_x, train_y)
    # Test model
    prediction_one = model_one.predict(test)
    # checked of score
    model_one.score(train_x, train_y)
    # print prediction
    return prediction_one


# In[97]:


def build_modele_two():
    train_x,test=Divide_data()
    train_y=bild_train_y()
    model_two = MultiOutputRegressor(Ridge(random_state=0))
    # Data training
    model_two.fit(train_x, train_y)
    # Test model
    prediction_two = model_two.predict(test)
    # checked of score
    model_two.score(train_x, train_y)
    # print prediction
    return prediction_two


# In[98]:


#read train file txt
def read_train():
    training_data = xgb.DMatrix(r"C:\\Users\\King\\Desktop\project_\\train00.txt")
    return training_data


# In[99]:


#read test file txt
def read_test():
    testing_data = xgb.DMatrix(r"C:\\Users\\King\\Desktop\project_\\train01.txt")
    return testing_data


# In[100]:


# list-wise
def build_model_three(training_data,testing_data):
    ltr_lambdamart_param = [('objective','rank:ndcg'),('max_depth',3), ('eta',0.1), ('seed',404)]
    #build model
    lambdamart_model = xgb.train(ltr_lambdamart_param, training_data)
    # test model
    pred_lambdamart = lambdamart_model.predict(testing_data)
    return pred_lambdamart


# In[101]:


#lambdarank (pairwise LTR)
def build_model_four(training_data,testing_data):
    ltr_lambdarank_param = [('objective','rank:pairwise'),('max_depth',3), ('eta',0.1), ('seed',404)]
    lambdarank_model = xgb.train(ltr_lambdarank_param, training_data)
    # test model
    pred_lambdarank = lambdarank_model.predict(testing_data)
    return pred_lambdarank


# In[102]:


# Function to calculate DCG
def DCG(rank,size):
    dcg=0
    sum=2
    for n in range(size,len(rank)):
        if n==size:
            dcg = dcg+rank[size]
        else:
            dcg=dcg+(rank[n]/math.log(sum,2))
            sum=sum+1
    return dcg


# In[103]:


#  calculate average NDCG for all quesries in the test file
def calculate_NDCG():
    training_data=read_train()
    testing_data=read_test()
    
    prediction_one=build_modele_one()
    prediction_tow=build_modele_two()
    pred_lambdamart=build_model_three(training_data,testing_data)
    pred_lambdarank=build_model_four(training_data,testing_data)
    
    #calculate NDCG to all modeles
    ndcg_model_one=DCG(prediction_one.round().flatten().astype(int),0)/DCG(train_df[0][400:],400)
    ndcg_model_two=DCG(prediction_tow.round().flatten().astype(int),0)/DCG(train_df[0][400:],400)
    ndcg_model_three=DCG(pred_lambdamart,0)/DCG(train_df[0][400:],400)
    ndcg_model_four=DCG(pred_lambdarank,0)/DCG(train_df[0][400:],400)
    
    return ndcg_model_one,ndcg_model_two,ndcg_model_three,ndcg_model_four


# In[104]:


def main():
    ndcg_model_one,ndcg_model_two,ndcg_model_three,ndcg_model_four=calculate_NDCG()
    return print(ndcg_model_one,ndcg_model_two,ndcg_model_three,ndcg_model_four)
    


# In[105]:


if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




