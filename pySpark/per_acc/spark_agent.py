# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 12:25:23 2017

@author: 10639497
"""
session = None
sql_context = None
hive_context = None
class Spark_Agent:
    def __init__(self):
        self.load_PySpark()
        from pyspark.sql import SparkSession
        from pyspark import SparkContext, SparkConf
        session = SparkSession.builder.appName("spark_agent_sess").getOrCreate()
        sql_context = SparkConf().setAppName("spark_agent_conf").setMaster("local") 
        
    def load_PySpark(self):
        import os
        import sys
        if 'SPARK_HOME' not in os.environ:
            os.environ['SPARK_HOME'] = 'D:/spark-2.1.1-bin-hadoop2.7/bin'
        SPARK_HOME = os.environ['SPARK_HOME']
        sys.path.insert(0,os.path.join(SPARK_HOME,"python"))
        sys.path.insert(0,os.path.join(SPARK_HOME,"python","pyspark"))
        sys.path.insert(0,os.path.join(SPARK_HOME,"python","py4j"))

def get_session():
    return session
def get_sql_context():
    return sql_context
def get_hive_context():
    return hive_context
def start_agent():
    Spark_Agent()
    
if __name__ == "__main__":
    start_agent()
    get_session()
