import mglearn
import matplotlib
from sklearn.datasets import load_iris
matplotlib.matplotlib_fname()
import matplotlib.pyplot as plt


'''iris= load_iris()
X= iris.data
print(type(X))
print(X.shape)
print(type(mglearn))'''
mglearn.plots.plot_scaling()
plt.suptitle("Scaling_data")
plt.show()