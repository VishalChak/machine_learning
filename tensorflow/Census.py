#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 19:22:58 2017

@author: vishal
"""
import tempfile
from urllib.request import urlretrieve

train_file= tempfile.NamedTemporaryFile()
test_file = tempfile.NamedTemporaryFile()

urlretrieve( "http://mlr.cs.umass.edu/ml/machine-learning-databases/adult/adult.data", train_file.name)
urlretrieve("http://mlr.cs.umass.edu/ml/machine-learning-databases/adult/adult.test", test_file.name)

import pandas as pd

COLUMNS = ["age", "workclass", "fnlwgt", "education", "education_num",
           "marital_status", "occupation", "relationship", "race", "gender",
           "capital_gain", "capital_loss", "hours_per_week", "native_country",
           "income_bracket"]

df_train = pd.read_csv(train_file, names=COLUMNS, skipinitialspace=True)
df_test = pd.read_csv(test_file, names=COLUMNS, skipinitialspace=True, skiprows=1)

import matplotlib
matplotlib.matplotlib_fname
import matplotlib.pyplot as plt

df_train.shape
df_test.shape

plt.show()
LABEL_COLUMN = "label"
df_train[LABEL_COLUMN] = (df_train["income_bracket"].apply(lambda x: ">50K" in x)).astype(int)
df_test[LABEL_COLUMN] = (df_test["income_bracket"].apply(lambda x: ">50K" in x)).astype(int)

CATEGORICAL_COLUMNS = ["workclass", "education", "marital_status", "occupation",
                       "relationship", "race", "gender", "native_country"]
CONTINUOUS_COLUMNS = ["age", "education_num", "capital_gain", "capital_loss", "hours_per_week"]

#Converting Data into Tensors


import tensorflow as tf

def input_fn(df):
    continuous_cols = {k: tf.constant(df[k].values)
                     for k in CONTINUOUS_COLUMNS}
    categorical_cols = {k: tf.SparseTensor(
      indices=[[i, 0] for i in range(df[k].size)],
      values=df[k].values,
      dense_shape=[df[k].size, 1])
                      for k in CATEGORICAL_COLUMNS}
    
    feature_cols = continuous_cols.copy()
    feature_cols.update(categorical_cols.copy())
    label = tf.constant(df[LABEL_COLUMN].values)
    
    return feature_cols, label

def train_input_fn():
  return input_fn(df_train)

def eval_input_fn():
  return input_fn(df_test)


gender = tf.contrib.layers.sparse_column_with_keys(column_name='gender', keys=["Female", "Male"])
education = tf.contrib.layers.sparse_column_with_hash_bucket(column_name="education", hash_bucket_size=1000)

workclass = tf.contrib.layers.sparse_column_with_hash_bucket(column_name='workclass', hash_bucket_size=100)
race = tf.contrib.layers.sparse_column_with_hash_bucket(column_name= 'race', hash_bucket_size=100)
marital_status= tf.contrib.layers.sparse_column_with_hash_bucket(column_name='marital_status', hash_bucket_size=100)
relationship = tf.contrib.layers.sparse_column_with_hash_bucket(column_name='relationship', hash_bucket_size=100)
native_country = tf.contrib.layers.sparse_column_with_hash_bucket(column_name='native_country', hash_bucket_size=1000)
occupation = tf.contrib.layers.sparse_column_with_hash_bucket(column_name='occupation', hash_bucket_size=1000)


age = tf.contrib.layers.real_valued_column('age')
education_num = tf.contrib.layers.real_valued_column('education_num')
capital_gain = tf.contrib.layers.real_valued_column('capital_gain')
capital_loss = tf.contrib.layers.real_valued_column('capital_loss')
hours_per_week = tf.contrib.layers.real_valued_column('hours_per_week')

age_buckets = tf.contrib.layers.bucketized_column(age, boundaries=[18, 25, 30, 35, 40, 45, 50, 55, 60, 65])

education_x_occupation = tf.contrib.layers.crossed_column([education, occupation], hash_bucket_size=int(1e4))

model_dir = tempfile.mkdtemp()

age_buckets_x_education_x_occupation = tf.contrib.layers.crossed_column([age_buckets, education_x_occupation],
                                                                        hash_bucket_size=int(1e4))

m = tf.contrib.learn.LinearClassifier(feature_columns=[gender, education, workclass, race, 
                                                       native_country,occupation, marital_status,
                                                       age_buckets,education_x_occupation,
                                                       age_buckets_x_education_x_occupation], model_dir=model_dir)
m.fit(input_fn=train_input_fn, steps=200)

results = m.evaluate(input_fn=eval_input_fn, steps=1)


for key in sorted(results):
    print("%s: %s" % (key, results[key]))

