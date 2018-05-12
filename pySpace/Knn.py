from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import numpy as np


class Knn:
	k = 1
	def load_data(self):
		iris = load_iris()
		X = iris.data
		y = iris.target
		z = iris.target_names
		return X,y,z

	def knnClassifier(self):
		X,y,z = self.load_data()
		clf = KNeighborsClassifier(n_neighbors = self.k)
		clf.fit(X,y)
		return clf,z
	
	def pridict(self):
		clf, tgtNms = self.knnClassifier()
		count = 1
		data = []
		while (count >0 and count <2):
			for i in range(4):
				data.append(float(input("Enter feature :")))
			testData = np.array(data)
			res = clf.predict(testData)
			print("Knn Predict that it is a : ",tgtNms[res[0]])
			data.clear()
			count = int(input("Enter 1 If you have Test Case "))



if __name__ == "__main__":
	print("This is KNN (K nearest neighbor) model and it is based on Iris data set(Default Data Set)")
	obj = Knn()
	k = int(input("Enter the value of K"))	
	obj.k = k	
	print("This Model will Pridict result {} nearest neighbor's Euclidean distance".format(obj.k))
	obj.pridict()
	
	
 
