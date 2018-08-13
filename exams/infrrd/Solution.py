#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 21:03:25 2018

@author: vishal
"""

import pandas as pd

base_path = '/home/vishal/datasets/exams/Infrrd/'

train_path = base_path + 'train.csv'
test_path = base_path + 'test.csv'

dataset = pd.read_csv(train_path)

dataset.head()

dataset.describe()