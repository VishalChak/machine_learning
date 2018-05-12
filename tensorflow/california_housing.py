#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 18:03:55 2017

@author: vishal
"""

from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing()

m ,n = housing.data.shape

import numpy as np
housing_data_plus_bias = np.c_[np.ones((m, 1)), housing.data]

import tensorflow as tf

X = tf.constant(housing_data_plus_bias,dtype = tf.float32, name="X")
y= tf.constant(housing.target.reshape(-1,1), dtype=tf.float32, name='y')

XT  = tf.transpose(X)
theta = tf.matmul(tf.matmul(tf.matrix_inverse(tf.matmul(XT,X)), XT),y)

with tf.Session() as sess:
    theta_val = theta.eval()
    
theta_val