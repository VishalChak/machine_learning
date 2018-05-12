#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 23:55:46 2017

@author: vishal
"""


import os
import sys

if 'SPARK_HOME' not in os.environ:
    print("I am inside")
    os.environ['SPARK_HOME'] = '/usr/sofwares/spark'
SPARK_HOME = os.environ['SPARK_HOME']
sys.path.insert(0,os.path.join(SPARK_HOME,"python"))
sys.path.insert(0,os.path.join(SPARK_HOME,"python","pyspark"))
sys.path.insert(0,os.path.join(SPARK_HOME,"python","py4j"))

from pyspark import SparkContext
from pyspark import SparkConf

from pyspark.ml import Pipeline
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.feature import HashingTF, Tokenizer

training = spark.createDataFrame([
    (0, "a b c d e spark", 1.0),
    (1, "b d", 0.0),
    (2, "spark f g h", 1.0),
    (3, "hadoop mapreduce", 0.0)
], ["id", "text", "label"])
