import mglearn
from sklearn.model_selection import train_test_split
import matplotlib
matplotlib.matplotlib_fname()
import matplotlib.pyplot as plt
import numpy as np


X, y = mglearn.datasets.load_extended_boston()

X_train,X_test,y_train, y_test = train_test_split(X,y)

arr = np.arange(30).reshape(10,3)
print(arr.shape)