
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np

knn = KNeighborsClassifier(n_neighbors=1)

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris['data'], iris['target'],random_state=0)

knn.fit(X_train, y_train)
X_new = np.array([[5, 2.9, 1, 0.2]])
prediction = knn.predict(X_new)
name  = iris['target_names'][prediction]
print(name)
#Evaluating the model

y_pred = knn.predict(X_test)

y_mean = np.mean(y_pred == y_test)
print(y_mean)
k_score = knn.score(X_test, y_test)
print(k_score)


