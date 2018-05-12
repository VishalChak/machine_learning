# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 15:19:30 2017

@author: appladmin
"""

from sklearn.datasets import load_sample_image
import matplotlib
import matplotlib.pyplot as plt

matplotlib.matplotlib_fname()
china = load_sample_image("china.jpg")
plt.plot(china)
plt.show()

