#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 18:56:50 2017

@author: vishal
"""

import tensorflow as tf
import pandas as pd

path ="/home/vishal/ML/datasets/HackerEarth/ZS/train.csv"

data = pd.read_csv(path)
data.describe()







