# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 12:25:23 2017

@author: 10639497
"""

class Robot:

    def __init__(self):
        self.load_PySpark()
        
    def load_PySpark(self):
        import os
        import sys
        if 'SPARK_HOME' not in os.environ:
            os.environ['SPARK_HOME'] = 'D:/spark-2.1.1-bin-hadoop2.7/bin'
        SPARK_HOME = os.environ['SPARK_HOME']
        sys.path.insert(0,os.path.join(SPARK_HOME,"python"))
        sys.path.insert(0,os.path.join(SPARK_HOME,"python","pyspark"))
        sys.path.insert(0,os.path.join(SPARK_HOME,"python","py4j"))


def start_agent():
    x = Robot()
if __name__ == "__main__":
    x = Robot()