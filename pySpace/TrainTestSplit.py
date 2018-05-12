from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split
import numpy as np

# Other Name Are
# Test Set Approch
# Validation Set Approch

class TrainTestSplit:

	def loadIrisData(self):
		iris = load_iris()
		X = iris.data
		y = iris.target
		z = iris.target_names
		return X,y,z
	
	#logisticRegretion
	def logiRegression(self,X,y):
		logreg = LogisticRegression()
		X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.4, random_state = 4)
		logreg.fit(X_train,y_train)                
		y_pred = logreg.predict(X_test)
		accu = metrics.accuracy_score(y_test,y_pred)
		print("Metrics Accuracy for logreg is : ",accu)
		
		
		
		
	
	#KNN k = n
	def knn(self,X,y,k):
		knn = KNeighborsClassifier(n_neighbors = k)
		X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.4, random_state = 4)
		knn.fit(X_train,y_train)
		y_pred = knn.predict(X_test)
		accu = metrics.accuracy_score(y_test,y_pred)
		print("Accuracy in KNN K {} is {}: ".format(k,accu))
	

if __name__ == "__main__":
	obj = TrainTestSplit()
	X,y,z = obj.loadIrisData()
	obj.logiRegression(X,y)
	obj.knn(X,y,5)
	obj.knn(X,y,1)
