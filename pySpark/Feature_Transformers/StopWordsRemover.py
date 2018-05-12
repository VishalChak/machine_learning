#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 16:23:10 2017

@author: vishal
"""

from __future__ import print_function

from pyspark.sql import SparkSession

session = SparkSession.builder.appName('StopWord').getOrCreate()

sentenceData = session.createDataFrame([
    (0, ["I", "saw", "the", "red", "balloon"]),
    (1, ["Mary", "had", "a", "little", "lamb"])
], ["id", "raw"])

sentenceData.show()

from pyspark.ml.feature import StopWordsRemover

remover = StopWordsRemover(inputCol="raw", outputCol="filtered")
remover.transform(sentenceData).show(truncate=False)

session.stop()

