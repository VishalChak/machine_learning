#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 22:21:51 2017

@author: vishal
"""
from __future__ import print_function

from pyspark.sql import SparkSession
session = SparkSession.builder.appName('DCT').getOrCreate()

from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import DCT


df = session.createDataFrame([
    (Vectors.dense([0.0, 1.0, -2.0, 3.0]),),
    (Vectors.dense([-1.0, 2.0, 4.0, -7.0]),),
    (Vectors.dense([14.0, -2.0, -5.0, 1.0]),)], ["features"])

dct = DCT(inverse=False, inputCol="features", outputCol="featuresDCT")

dctDf = dct.transform(df)

dctDf.select("featuresDCT").show(truncate=False)

session.stop()