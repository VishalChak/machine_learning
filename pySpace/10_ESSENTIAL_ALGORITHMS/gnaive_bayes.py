from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris

class Naive_Bayes:
	def __init__(self):
		iris = load_iris()
		self.X= iris.data
		self.y = iris.target
		self.z = iris.target_names
		self.gnb = GaussianNB()
		self.gnb.fit(self.X,self.y)
	def gnb_prediction(self, data):
		y_pred = self.gnb.predict(data)
		if len(y_pred) == 1:
			print(self.z[y_pred[0]])
		else :
			print(y_pred)

if __name__ == "__main__" : 
	obj = Naive_Bayes()
	print("This is gaussianNaiveBayes classifier on Iris data set")
	temp = int((input("Press 1 to predict ")))
	while temp ==1 :
		X_test = []
		for i in range(4):
			X_test.append(int(input("  Enter Featue")))
		obj.gnb_prediction(X_test)
		temp = int((input("Press 1 to predict ")))
