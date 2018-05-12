import numpy as np

from sklearn.decomposition import PCA

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
print(X)
pca = PCA(n_components=2)
pca.fit(X)
print(pca)
print(pca.explained_variance_ratio_) 

pca = PCA(n_components=2, svd_solver='full')
pca.fit(X)
print(pca)
print(pca.explained_variance_ratio_) 

'''pca = PCA(n_components=1, svd_solver='arpack')
pca.fit(X)
print(pca)
print(pca.explained_variance_ratio_) '''

X_new = pca.fit_transform(X)
#print(X_new)

covariance = pca.get_covariance()
print(covariance)

params = pca.get_params(deep=True)
print(params)

data = pca.inverse_transform(X_new, y=None)
print(data)



