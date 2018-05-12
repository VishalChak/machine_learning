#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 19:59:05 2017

@author: vishal
"""


from __future__ import print_function

from pyspark.sql import SparkSession

session = SparkSession.builder.appName("Binarizer").getOrCreate()


continuousDataFrame = session.createDataFrame([(0, 0.1),
                                               (1, 0.8),
                                               (2, 0.2)],
                                                ["id", "feature"])

#continuousDataFrame.show()

from pyspark.ml.feature import Binarizer

binarizer = Binarizer(threshold = 0.5, inputCol = 'feature', outputCol = 'binarized_feature')

binarizedDataFrame = binarizer.transform(continuousDataFrame)
binarizedDataFrame.show()

session.stop()