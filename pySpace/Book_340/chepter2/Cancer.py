import mglearn
import matplotlib
matplotlib.matplotlib_fname()
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

X, y = mglearn.datasets.make_forge()
plt.scatter(X[:, 0], X[:, 1], c=y, s=60, cmap=mglearn.cm2)

X, y = mglearn.datasets.make_wave(n_samples=40)
plt.plot(X, y, 'o')
plt.plot(X, -3 * np.ones(len(X)), 'o')
plt.ylim(-3.1, 3.1)
#plt.show()

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()
keys = cancer.keys()
print(keys)

#print(cancer.feature_names)
print(cancer.target_names)

bincount = np.bincount(cancer.target)
print(bincount)


from sklearn.datasets import load_boston
boston = load_boston()
print(boston.keys())
print(boston.feature_names)
print(boston.target)

X, y = mglearn.datasets.load_extended_boston()
print(X.shape)

#mglearn.plots.plot_knn_classification(n_neighbors=1)
mglearn.plots.plot_knn_classification(n_neighbors=3)
plt.title("forge_one_neighbor");
plt.show()

for n_neighbors, ax in zip([1, 3, 9], axes):
# make predictions using 1, 3 or 9 neighbors
    reg = KNeighborsRegressor(n_neighbors=n_neighbors).fit(X, y)
    ax.plot(X, y, 'o')
    ax.plot(X, -3 * np.ones(len(X)), 'o')
    ax.plot(line, reg.predict(line))
    ax.set_title("%d neighbor(s)" % n_neighbors)
plt.show()