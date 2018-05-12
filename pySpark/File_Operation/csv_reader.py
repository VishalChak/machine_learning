#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 22:36:58 2017

@author: vishal
"""

from __future__ import print_function

from pyspark.sql import SparkSession

session = SparkSession.builder.appName('DCT').getOrCreate()

path = "/home/vishal/ML/PySpark/Test.csv"
df = session.read.option('inferschema', True).option('header', True).csv(path)
df.printSchema()
df.show()
session.stop()