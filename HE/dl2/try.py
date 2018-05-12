# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:42:59 2018

@author: 10639497
"""

from zipfile import ZipFile
from PIL import Image # $ pip install pillow

path = "D:\\Vishal\\Dataset\\HE\\dl2\\Zars\\"
filename = path + "dl2_trimages.zip"


from zipfile import ZipFile

help(ZipFile)
with ZipFile(filename, 'r') as zip:
    print(zip.read())
    print(type(zip.printdir()))
    # printing all the contents of the zip file
    for img, date_, size in zip.printdir():
        print (img)
 
    # extracting all the files
    print('Extracting all the files now...')
    zip.extractall()
    print('Done!')