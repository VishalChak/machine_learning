import pylab as plt
import numpy as np
from scipy.spatial.distance import cdist,pdist
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

'''iris = load_iris()

k= range(1,11)

clusters = [KMeans(n_clusters = c,init = 'k-means++').fit(iris.data) for c in k]
centr_lst = [cc.cluster_centers_ for cc in clusters]

k_distance = [cdist(iris.data,cent,'euclidean') for cent in centr_lst]
clust_indx  = [np.argmin(kd,axis=1) for kd in k_distance]
distances = [np.min(kd,axis=1) for kd in k_distance]
avg_within= [np.sum(dist)/iris.data.shape[0] for dist in distances]

kidx = 2

fig = plt.figure()
ax =  fig.add_subplot(111)
ax.plot(k,avg_within,'g*-')
ax.plot(k[kidx],avg_within[kidx],marker='o',markersize=12, markeredgewidth=2 ,markeredgecolor='r' , markerfacecolor='None')
plt.grid(True)
plt.xlabel('No of clusters')
plt.ylabel('Avg within-cluster sum of squares')'''

###Clustering for IRIS data #unsupervised

from sklearn import cluster,datasets
from sklearn import metrics
iris = datasets.load_iris()
k_means = cluster.KMeans(n_clusters=3)
kmf=k_means.fit(iris.data)

y_kmeans = kmf.predict(iris.data)

plt.scatter(iris.data[:,0],iris.data[:,1], c=y_kmeans , s=50,cmap='rainbow')



from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_iris

iris = load_iris()

X, y = iris.data, iris.target

X_train , X_test, y_train, y_test = train_test_split(X,y)
kMeans = cluster.KMeans(n_clusters = 3)
kMeans.fit(X_train, y_train)
y_pred = kMeans.predict(X_test)
from sklearn.metrics import confusion_matrix
score = confusion_matrix(y_test, y_pred)
print(score)




