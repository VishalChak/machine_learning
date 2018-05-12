#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 00:08:47 2017

@author: vishal
"""
path = "/home/vishal/ML/datasets/Iris.csv"

import pandas as pd

data = pd.read_csv(path, names = ["A", "B", "C", "E"])

X = data
X_centered  =X - X.mean(axis=0)

X_centered.head()

import numpy as np
U, s, V = np.linalg.svd(X_centered)

c1 = V.T[:, 0]
c2 = V.T[:, 1]

W2 = V.T[:, :2]
X2D = X_centered.dot(W2)