# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 11:50:14 2017

@author: 10639497
"""
import spark_agent
def exe():
    spark_agent.start_agent()
    sess = spark_agent.get_session
    print(sess)

if __name__ == "__main__":
    exe()
    
    