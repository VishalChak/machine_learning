#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 12:05:45 2017

@author: vishal
"""

from sklearn.datasets import fetch_20newsgroups

twenty_train = fetch_20newsgroups(subset='train', shuffle=True)


print(twenty_train)

twenty_train = fetch_20newsgroups(subset='train', shuffle=True)
twenty_train.target_names

print("\n".join(twenty_train.data[0].split('\n')[:3]))

print("\n".join(twenty_train.data[0].split("\n")[:3]))