#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 21:00:59 2017

@author: vishal
"""

from __future__ import print_function
from pyspark.sql import SparkSession

session = SparkSession.builder.appName('Polynomial Expension').getOrCreate()

from pyspark.ml.linalg import Vectors

df = session.createDataFrame([
    (Vectors.dense([2.0, 1.0]),),
    (Vectors.dense([0.0, 0.0]),),
    (Vectors.dense([3.0, -1.0]),)
], ["features"])

#df.show()
from pyspark.ml.feature import PolynomialExpansion

polyExpansion = PolynomialExpansion(degree = 2, inputCol = "features",
                                    outputCol = "pe_feature")

ps_df = polyExpansion.transform(df)
print(df.first())
print(ps_df.first())


#ps_df.select('pe_feature').show()

session.stop()