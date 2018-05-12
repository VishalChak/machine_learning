from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import numpy as np

class TrainAndTest:
	
	def loadIrisData(self):
		iris = load_iris()
		X = iris.data
		y = iris.target
		z = iris.target_names
		return X,y,z
	
	#logisticRegretion
	def logiRegression(self,X,y):
		logreg = LogisticRegression()
		logreg.fit(X,y)
		y_pred = logreg.predict(X)
		accur = metrics.accuracy_score(y,y_pred)
		print("Metrics Accuracy for logreg is : ",accur)
		
		
	
	#KNN k = n
	def knn(self,X,y,k):
		knn = KNeighborsClassifier(n_neighbors = k)
		knn.fit(X,y)
		y_pred = knn.predict(X)
		accu = metrics.accuracy_score(y,y_pred)
		print("Accuracy in KNN K {} is {}: ".format(k,accu))
	

if __name__ == "__main__":
	obj = TrainAndTest()
	X,y,z = obj.loadIrisData()
	obj.logiRegression(X,y)
	obj.knn(X,y,5)
	obj.knn(X,y,1)
	
	
