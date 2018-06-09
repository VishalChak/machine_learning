# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 19:00:35 2018

@author: 10639497
"""
import feature_engineering, spark_master
from pyspark.ml.linalg import Vectors


if __name__ == "__main__":
    path = 'D:\\datasets\\AV\\Sentiment_analysis\\train_.csv'
    path_titanic = 'D:\datasets\titanic'
    
    session  = spark_master.getSession()
    dataset = session.read.csv(path, header='true', inferSchema='true')
    print('tokenizer')
    dataset = feature_engineering.tokenizer(dataset, 'tweet')
    dataset.show()
    dataset = feature_engineering.regexTokenizer(dataset,'tweet' )
    dataset = feature_engineering.stopWordsRemover(dataset, 'tweet_rgxtkn')
    dataset = feature_engineering.nGram(dataset,'tweet_rgxtkn')
    
    continuousDataFrame = session.createDataFrame([(0, 0.1),(1, 0.8),(2, 0.2)], ["id", "feature"])
    continuousDataFrame = feature_engineering.binarizer(continuousDataFrame,'feature')
    continuousDataFrame.show()
    
    data = [(Vectors.sparse(5, [(1, 1.0), (3, 7.0)]),),
        (Vectors.dense([2.0, 0.0, 3.0, 4.0, 5.0]),),
        (Vectors.dense([4.0, 0.0, 0.0, 6.0, 7.0]),)]
    df = session.createDataFrame(data, ["features"])
    df , model= feature_engineering.pca(df, 'features')
    df = feature_engineering.polynomial_expansion(df, 'features')
    df = feature_engineering.dct(df,'features')
    df.show()
    
    df = session.createDataFrame(
    [(0, "a"), (1, "b"), (2, "c"), (3, "a"), (4, "a"), (5, "c")],
    ["id", "category"])
    
    df, model = feature_engineering.string_indexer(df, 'category')
    df.show()
    
    df = feature_engineering.index_to_string(df, 'category_si')
    df.show()
    
    df = feature_engineering.one_hot_encoder_estimator(df, )