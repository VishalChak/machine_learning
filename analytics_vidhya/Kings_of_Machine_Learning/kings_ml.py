# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 12:41:52 2018

@author: 10639497
"""

import pandas as pd

project = "Kings_of_Machine_Learning"
path = "D:/Vishal/Dataset/AV/" + project

hero_data_path = path+ "/hero_data.csv"
train1_path = path+ "/train1.csv"
train9_path = path+ "/train9.csv"

hero_data = pd.read_csv(hero_data_path)
hero_data.head()

train1_data = pd.read_csv (train1_path)
train1_data.head()

train9_data = pd.read_csv (train9_path)
train9_data.head()