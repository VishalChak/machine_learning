# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 15:04:58 2018

@author: 10639497
"""

from pyspark.sql import SparkSession


session = None

def getSession():
    global session
    if session == None:
        session = SparkSession.builder.appName("master").getOrCreate()
    return session
