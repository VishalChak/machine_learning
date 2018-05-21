#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 23:52:54 2018

@author: vishal
"""

import pandas as pd
import nltk
path = "/home/vishal/datasets/machine_hack/How-To-Choose-The-Perfect-Beer-Data-Set/train.csv"

dataset = pd.read_csv(path)

dataset.shape
dataset.dtypes

dataset.head()

dataset['Food Paring'].head()
min(dataset['Score'])


import numpy as np
import pandas as pd
from scipy import stats, integrate
import matplotlib.pyplot as plt

import seaborn as sns
sns.set(color_codes=True)

np.random.seed(sum(map(ord, "distributions")))

x = np.random.normal(size=100)

sns.distplot(dataset['Score'])

dataset.isnull().count()

sns.boxplot(data=dataset);
sns.violinplot(data=dataset)