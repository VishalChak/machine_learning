from sklearn import tree
from sklearn.datasets import load_iris

class DecisionTree:
	def load_iris_dataset(self):
		iris = load_iris()
		self.X = iris.data
		self.y = iris.target
		self.z = iris.target_names
	def train_model(self):
		self.clf = tree.DecisionTreeClassifier()
		self.clf.fit(self.X,self.y)
	def prediction(self,data):
		y_pred = self.clf.predict(data)
		print(self.z[y_pred[0]])
		
if __name__ == "__main__":
	obj = DecisionTree()
	
	print("THis is decision Tree Classfiers")
	x = int(input("Enter 1 to pridect "))
	obj.load_iris_dataset()	
	obj.train_model()
	while x == 1 :
		data = []
		for i in range (4):
			data.append(int(input("Enter featue")))
		obj.prediction(data)
		x = int(input("Enter 1 to pridect "))
