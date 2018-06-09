# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 14:12:52 2018

@author: 10639497
"""

##########Transformer##########

def tokenizer(dataset, inputCol):
    from pyspark.ml.feature import Tokenizer
    return Tokenizer(inputCol=inputCol, outputCol=inputCol+'_tkn').transform(dataset)

def regexTokenizer (dataset, inputCol, pattern = '\\W'):
    from pyspark.ml.feature import RegexTokenizer
    return RegexTokenizer(inputCol=inputCol, outputCol=inputCol+'_rgxtkn', pattern=pattern).transform(dataset)
    
def stopWordsRemover(dataset, inputCol):
    from pyspark.ml.feature import StopWordsRemover
    return StopWordsRemover(inputCol=inputCol, outputCol=inputCol+'_swr').transform(dataset)

def nGram(dataset, inputCol, ngram = 2):
    from pyspark.ml.feature import NGram
    return NGram(n = ngram, inputCol=inputCol, outputCol=inputCol+'_ngram').transform(dataset)

def binarizer (dataset, inputCol, threshold=0.5):
    from pyspark.ml.feature import Binarizer
    return Binarizer(threshold=threshold, inputCol=inputCol, outputCol=inputCol + "_binarized").transform(dataset)

def polynomial_expansion(dataset, inputCol, degree = 3):
    from pyspark.ml.feature import PolynomialExpansion
    return PolynomialExpansion(degree=degree, inputCol=inputCol, outputCol=inputCol+'_pe').transform(dataset)

def dct (dataset,inputCol, inverse = False):
    from pyspark.ml.feature import DCT
    return DCT(inverse=inverse, inputCol=inputCol, outputCol=inputCol+'_dct').transform(dataset)

def index_to_string(dataset, inputCol):
    from pyspark.ml.feature import IndexToString
    return IndexToString(inputCol=inputCol, outputCol=inputCol+'_i2s').transform(dataset)

##########Estimator##########

def pca(dataset, inputCol, k=3):
    from pyspark.ml.feature import PCA
    model = PCA(k=3, inputCol=inputCol, outputCol=inputCol+'_pca').fit(dataset)
    return model.transform(dataset), model

def string_indexer(dataset, inputCol):
    from pyspark.ml.feature import StringIndexer
    model = StringIndexer(inputCol=inputCol, outputCol=inputCol+'_si').fit(dataset)
    return model.transform(dataset), model
    
    ## We can give multiple columns at once 
    ##inputCols=["categoryIndex1", "categoryIndex2"],
    ##outputCols=["categoryVec1", "categoryVec2"]
def one_hot_encoder_estimator(dataset,inputCols,outputCols = None):
    from pyspark.ml.feature import OneHotEncoderEstimator
    if outputCols == None:
        outputCols = inputCols + '_ohee'
    model = OneHotEncoderEstimator(inputCols=inputCols, outputCols=outputCols).fit(dataset)
    return model.transform(dataset), model