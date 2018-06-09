# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 16:09:33 2017

@author: 10639497
"""

import pandas as pd
import numpy as np

def remove_outlier(dataset):
    num_dataset, other_dataset = dividedata(dataset)
    low = .05
    high = .95
    quant_df = num_dataset.quantile([low, high])
    num_dataset.apply(lambda x: x[(x>quant_df.loc[low,x.name]) & 
                                    (x < quant_df.loc[high,x.name])], axis=0)
    filt_df =  pd.concat([num_dataset,other_dataset], axis=1)
    #filt_df.dropna(inplace=True)
    return filt_df
    

def dividedata(dataset):
    data_schema = dataset.dtypes
    num_list = []
    other_list = []
    for index, val in data_schema.iteritems():
        #print(index,val)
        isTrue = np.issubdtype(val, np.number)
        #print(isTrue)
        if isTrue:
            num_list.append(index)
        else:
            other_list.append(index)
    print(num_list)
    print(other_list)
    num_dataset = dataset[num_list]
    other_dataset = dataset[other_list]
    return num_dataset, other_dataset

path = "D:/Vishal/Kaggle/Titanic/train.csv"
dataset = pd.read_csv(path)
data = remove_outlier(dataset)
'''print(dataset.shape)
print(data.head())'''

