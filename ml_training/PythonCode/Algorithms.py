
# coding: utf-8

# In[8]:

##Linear regression

import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr   

X=[[6],[8],[10],[14],[18]]
y=[[7],[9],[13],[17.5],[18]]
print pearsonr(X,y)
plt.figure()
plt.title('Pizza price plotted against diameter')
plt.xlabel('Diameter in inches')
plt.ylabel('Price in dollars')
plt.plot(X,y,'k.')
plt.axis([0,25,0,25])
plt.grid(True)
plt.show()


# In[9]:

from sklearn.linear_model import LinearRegression
X=[[6],[8],[10],[14],[18]]
y=[[7],[9],[13],[17.5],[18]]
X_test=[[8],[9],[11],[16],[12]]
y_test=[[11],[8.5],[15],[18],[11]]
model=LinearRegression()
model.fit(X,y)

print'R-squared:%.4f'%model.score(X_test,y_test)
#The coefficients
print'Coefficients:/n',model.coef_


# In[ ]:




# In[10]:

# Logistic Regression
from sklearn import datasets
from sklearn import metrics
from sklearn.linear_model import LogisticRegression

# load the iris datasets
dataset = datasets.load_iris()

# fit a logistic regression model to the data
model = LogisticRegression()
model.fit(dataset.data, dataset.target)
print(model)




# make predictions
expected = dataset.target
predicted = model.predict(dataset.data)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))




# In[33]:

###single tree

from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn import datasets

iris = datasets.load_iris()

clf = DecisionTreeClassifier(max_depth=1,criterion="entropy") # construct a decision tree.
clf.fit(iris.data,iris.target)  # train it on the dataset


with open("C:/MJ_Syn/Manisha_Notes/Training/iris.jpg", 'w') as f:
 f = tree.export_graphviz(clf, out_file=f)

#import os
#os.unlink('iris.pdf')


# In[13]:

get_ipython().system(u'pip install pydot pip install graphviz')


# In[31]:

import pydotplus 
dot_data = tree.export_graphviz(clf, out_file=None) 
graph = pydotplus.graph_from_dot_data(dot_data) 
graph.write_pdf("iris.pdf") 


# In[15]:

print clf


# In[16]:

#Random Forest
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np


# In[17]:

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
df.head()

train, test = df[df['is_train']==True], df[df['is_train']==False]


# In[18]:

features = df.columns[:4]
clf = RandomForestClassifier(n_jobs=2)
y, _ = pd.factorize(train['species'])
clf.fit(train[features], y)

preds = iris.target_names[clf.predict(test[features])]
pd.crosstab(test['species'], preds, rownames=['actual'], colnames=['preds'])


# In[19]:

###Standard Import
get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# use seaborn plotting defaults
import seaborn as sns; sns.set()


# In[20]:

import pylab as plt
import numpy as np
from scipy.spatial.distance import cdist, pdist
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

iris = load_iris()
k = range(1,11)

clusters = [KMeans(n_clusters = c,init = 'k-means++').fit(iris.data) 
            for c in k]
centr_lst = [cc.cluster_centers_ for cc in clusters]

k_distance = [cdist(iris.data, cent, 'euclidean') for cent in centr_lst]
clust_indx = [np.argmin(kd,axis=1) for kd in k_distance]
distances = [np.min(kd,axis=1) for kd in k_distance]
avg_within = [np.sum(dist)/iris.data.shape[0] for dist in distances]

kidx = 2

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(k, avg_within, 'g*-')
ax.plot(k[kidx], avg_within[kidx], marker='o', markersize=12, markeredgewidth=2, markeredgecolor='r', markerfacecolor='None')
plt.grid(True)
plt.xlabel('Number of clusters')
plt.ylabel('Average within-cluster sum of squares')
plt.title('Elbow for KMeans clustering (IRIS Data)')
#with_in_sum_square = [np.sum(dist ** 2) for dist in distances]
#to_sum_square = np.sum(pdist(iris.data) ** 2)/iris.data.shape[0]
#bet_sum_square = to_sum_square - with_in_sum_square


# In[21]:

####Clustering for IRIS data =====#Unsupervised======
from sklearn import cluster, datasets
from sklearn import metrics
iris = datasets.load_iris()
k_means = cluster.KMeans(n_clusters=3)
kmf=k_means.fit(iris.data)

y_kmeans = kmf.predict(iris.data)

plt.scatter(iris.data[:, 0], iris.data[:, 1], c=y_kmeans, s=50,
            cmap='rainbow');


# In[22]:

from fig_code import plot_kmeans_interactive
plot_kmeans_interactive();


# In[23]:

#KNN
from sklearn import datasets

import pandas as pd
import numpy as np


# load the iris datasets
iris = datasets.load_iris()
type(iris)


# In[24]:

from sklearn.cross_validation import train_test_split

# create design matrix X and target vector y
X = iris.data[:, :4] 
y = iris.target 

# split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


# In[25]:

# creating odd list of K for KNN
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
myList = list(range(1,50))

# subsetting just the odd ones
neighbors = filter(lambda x: x % 2 != 0, myList)

# empty list that will hold cv scores
cv_scores = []

# perform 10-fold cross validation
for k in neighbors:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_train, y_train, cv=10, scoring='accuracy')
    cv_scores.append(scores.mean())


# In[26]:

import matplotlib.pylab as plt


# changing to misclassification error
MSE = [1 - x for x in cv_scores]

# determining best k
optimal_k = neighbors[MSE.index(min(MSE))]
print "The optimal number of neighbors is %d" % optimal_k

# plot misclassification error vs k
plt.plot(neighbors, MSE)
plt.xlabel('Number of Neighbors K')
plt.ylabel('Misclassification Error')
plt.show()


# In[27]:

# loading library
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# instantiate learning model (k = 7)
knn = KNeighborsClassifier(n_neighbors=7)

# fitting the model
knn.fit(X_train, y_train)

# predict the response
pred = knn.predict(X_test)

# evaluate accuracy
print accuracy_score(y_test, pred)

# or predict on a specific examples!
print(knn.predict(X_test[5:10]))
print(y_test[5:10]) 


# In[ ]:



