#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 20:48:04 2017

@author: vishal
"""


from __future__ import print_function

from pyspark.sql import SparkSession

session = SparkSession.builder.appName('PCA').getOrCreate()

from pyspark.ml.linalg import Vectors

data = [(Vectors.sparse(5, [(1, 1.0), (3, 7.0)]),),
        (Vectors.dense([2.0, 0.0, 3.0, 4.0, 5.0]),),
        (Vectors.dense([4.0, 0.0, 0.0, 6.0, 7.0]),)]

data_frame = session.createDataFrame(data, ['features'])
#data_frame.show()

from pyspark.ml.feature import PCA

pca  = PCA(inputCol ='features', outputCol = "pca_feature", k=3)
model = pca.fit(data_frame)
pca_df  = model.transform(data_frame)

pca_df.show()


session.stop()