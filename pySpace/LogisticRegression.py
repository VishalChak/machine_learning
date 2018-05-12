from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import numpy as np


class LogisticRegressionClassifier:
	def load_data(self):
		iris = load_iris()
		X = iris.data
		y = iris.target
		z = iris.target_names
		return X,y,z

	def classifier(self):
		X,y,z = self.load_data()
		clf = LogisticRegression()
		clf.fit(X,y)
		return clf,z
	
	def pridict(self):
		clf, tgtNms = self.classifier()
		count = 1
		data = []
		while (count >0 and count <2):
			for i in range(4):
				data.append(float(input("Enter feature :")))
			testData = np.array(data)
			res = clf.predict(testData)
			print("logisticRegression Predict that it is a : ",tgtNms[res[0]])
			data.clear()
			count = int(input("Enter 1 If you have Test Case "))



if __name__ == "__main__":
	print("This Logictic Regression classifier model and it is based on Iris data set(Default Data Set)")
	obj = LogisticRegressionClassifier()	
	obj.pridict()
	
	
 
