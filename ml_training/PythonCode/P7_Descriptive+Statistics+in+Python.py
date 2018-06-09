
# coding: utf-8



# View first 20 rows
import pandas
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
peek = data.head()
print(peek)




# Dimensions of your data
shape = data.shape
print(shape)




# Data Types for Each Attribute

types = data.dtypes
print(types)




# Statistical Summary

pandas.set_option('display.width', 100)
pandas.set_option('precision', 3)
description = data.describe()
print(description)




# Class Distribution

class_counts = data.groupby('class').size()
print(class_counts)




# Pairwise Pearson correlations

correlations = data.corr(method='pearson')
print(correlations)




# Skew for each attribute

skew = data.skew()
print(skew)


# The skew result show a positive (right) or negative (left) skew. Values closer to zero show less skew.




