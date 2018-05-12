import mglearn
import matplotlib
matplotlib.matplotlib_fname()
import matplotlib.pyplot as plt
import numpy as np


from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()


#Step 1:

'''mglearn.plots.plot_pca_illustration()
plt.show()'''

#Step 2 :


'''
keys = cancer.keys()
fig , axes = plt.subplots(15,2, figsize=(10,20))
malignant = cancer.data[cancer.target == 0]
benign = cancer.data[cancer.target == 1]
ax = axes.ravel()
for i in range(30):
	_, bins = np.histogram(cancer.data[:, i], bins=50)
	ax[i].hist(malignant[:, i], bins=bins, color='b', alpha=.5)
	ax[i].hist(benign[:, i], bins=bins, color='r', alpha=.5)
	ax[i].set_title(cancer.feature_names[i])
	ax[i].set_yticks(())
fig.tight_layout()
plt.suptitle("cancer_histograms")
plt.show() '''

#Step 3 :

from sklearn.preprocessing import StandardScaler
#print(cancer.data)
X = cancer.data
scaler = StandardScaler()
scaler.fit(X)
X_scaled = scaler.transform(X)
print(X.max())
print(X_scaled.max())
print(X.min())
print(X_scaled.min())

# step4

from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
pca.fit(X_scaled)

X_pca = pca.transform(X_scaled)
print("Original shape: %s" % str(X_scaled.shape))
print("Reduced shape: %s" % str(X_pca.shape))

'''plt.figure(figsize=(8, 8))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=cancer.target, cmap=mglearn.tools.cm, s=60)
plt.gca().set_aspect('equal', adjustable='box')
#plt.axis('scaled')
plt.xlabel("First principal component")
plt.ylabel("Second principal component")
#plt.show()
print(pca.components_.shape)
print(pca.components_)'''

# Step 5

# Plot First vs second principle component analysis, color by call 
plt.matshow(pca.components_,cmap='viridis')
plt.yticks([0, 1], ["first component", "second component"])
plt.colorbar()
plt.xticks(range(len(cancer.feature_names)),
	cancer.feature_names, rotation=60, ha='left');
plt.suptitle("pca_components_cancer")
plt.show()



