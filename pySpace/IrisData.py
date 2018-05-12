import numpy as np
from sklearn.datasets import load_iris

class IrisData:
	def load_iris_data():
		iris = load_iris()
		X = iris.data
		y = iris.target
		z = iris.target_names
		return X,y,z
