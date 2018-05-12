#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 20:07:28 2017

@author: vishal
"""


import pandas as pd
from datetime import datetime, timedelta

path = "/home/vishal/ML/"

IDdata = pd.read_csv(path+"IDMapping.txt", sep='|', index_col=False)


IDdata['StartDate'] = pd.to_datetime(IDdata['StartDate'], format='%Y%m%d')
IDdata['EndDate'] = pd.to_datetime(IDdata['EndDate'], format='%Y%m%d')
Adata = pd.read_csv(path+"AssetIdentity.txt" , sep='|',index_col=False)

while(1):
    print('\n')
    opt = input("Select Option\n 1.SEDOL\n 2.CUSIP\n 3.ISIN\n")
    rootId = input("Enter RootID\n")
    s = input("Enter date YYYYMMDD")
    date = datetime(year=int(s[0:4]), month=int(s[4:6]), day=int(s[6:8]))
    data = None
    if opt == '1':
        data = IDdata.loc[(IDdata['AssetIDType'] == 'SEDOL') & (IDdata['StartDate'] <= date) & (IDdata['EndDate'] >= date)]
    elif opt == '2' :
        data = IDdata.loc[(IDdata['AssetIDType'] == 'CUSIP') & (IDdata['StartDate'] <= date) & (IDdata['EndDate'] >= date)]
    elif opt == '3':
        data = IDdata.loc[(IDdata['AssetIDType'] == 'ISIN') & (IDdata['StartDate'] <= date) & (IDdata['EndDate'] >= date)]
        
    data1 = Adata.loc[(Adata['RootID'] == rootId)]
    uniID = data1['S2ID']
    res = data.loc[(data['S2ID']).isin(uniID)]
    print(res['S2ID'])
    