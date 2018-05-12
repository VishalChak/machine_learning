import os
import sys
os.chdir('D:\Pyspark_Workspace')
os.curdir

if 'SPARK_HOME' not in os.environ:
    os.environ['SPARK_HOME'] = 'D:\Spark\spark-2.0.2-bin-hadoop2.7'
    
SPARK_HOME = os.environ['SPARK_HOME']

sys.path.insert(0,os.path.join(SPARK_HOME,"python"))
sys.path.insert(0,os.path.join(SPARK_HOME,"python","pyspark"))
sys.path.insert(0,os.path.join(SPARK_HOME,"python","py4j"))


print(sys.path)


import pyspark as ms

from pyspark import SparkContext
from pyspark import SparkConf

