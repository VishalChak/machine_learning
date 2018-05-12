# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 18:16:08 2017

@author: 10639497
"""

import zipfile

import requests
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as ptl

r = requests.post('http://www.transtats.bts.gov/DownLoad_Table.asp?Table_ID=236&Has_Group=3&Is_Zipped=0',stream=True)

with open("flights.csv", 'wb') as f:
    for chunk in r.iter_content(chunk_size=1024):
        if (chunk):
            f.write(chunk)

