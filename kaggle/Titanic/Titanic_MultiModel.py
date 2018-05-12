import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import numpy as np

class Titanic:
	def read_csv(self,filePath):
		data = pd.read_csv(filePath)
		return data
	def feature_selection(self, data):
		feature_cols = ['Pclass','Sex','Age', 'SibSp', 'Parch']
		X = data[feature_cols]
		X.loc[X['Sex'] == 'male', 'Sex'] = 1
		X.loc[X['Sex'] == 'female', 'Sex'] = 0
		X["Age"].fillna(X["Age"].mean(), inplace=True)
		return X

	def tunning(self,X,y):
		k_scores = []
		k_range = range(1,31)
		for k in k_range:
			knn = KNeighborsClassifier(n_neighbors = k)
			scores = cross_val_score(knn,X,y,cv = 10,scoring = 'accuracy')
			k_scores.append(scores.mean())
		return k_scores.index(max(k_scores))

	def knn_model(self,train_fp):
		data = self.read_csv(train_fp)
		X = self.feature_selection(data)
		y = data['Survived']	
		k = self.tunning(X,y)
		knn = KNeighborsClassifier(n_neighbors = k)
		knn.fit(X,y)
		return knn
	
	def logreg_model(self,train_fp):
		data = self.read_csv(train_fp)
		X = self.feature_selection(data)
		y = data['Survived']
		logreg = LogisticRegression()
		logreg.fit(X,y)
		return logreg

	def accuracy_test(self,train_fp,test_fp, gen_fp):
		res_data = self.read_csv(gen_fp)
		y_gen = res_data['Survived']
		#nd_gen = np.nanmin(res_data['Survived'].values)
		test_data = self.read_csv(test_fp)
		X_test = self.feature_selection(test_data)
		knn = self.knn_model(train_fp)
		logreg = self.logreg_model(train_fp)
		y_pred_knn = knn.predict(X_test)
		y_pred_logreg = logreg.predict(X_test)
		#print(y_pred_logreg)		
		knn_acc = metrics.accuracy_score(y_gen,y_pred_knn)
		logreg_acc = metrics.accuracy_score(y_gen,y_pred_logreg)
		if knn_acc > logreg_acc :
			return knn
		else : 
			return logreg
	
	def prediction(self,clf,test_fp,res_fp):
		data = self.read_csv(test_fp)
		X = self.feature_selection(data)
		y_pred = clf.predict(X)
		#np.hstack([y_pred, np.array(range(418)).reshape(2,1)])
		y_pred  = np.c_[np.arange(892,1310), y_pred]
		np.savetxt(res_fp, y_pred, delimiter=",", fmt='%d', header="PassengerId,Survived")
		print("Reponce Saved in : ", res_fp)
		
		
if __name__ == "__main__":
	obj = Titanic()
	train_fp = "/home/vishal/ML/Kaggle_Competition/Titanic/train.csv"
	test_fp = "/home/vishal/ML/Kaggle_Competition/Titanic/test.csv"
	res_fp = "/home/vishal/ML/Kaggle_Competition/Titanic/responce.csv"
	gen_fp = "/home/vishal/ML/Kaggle_Competition/Titanic/gender_submission.csv"
	clf = obj.accuracy_test(train_fp,test_fp,gen_fp)
	obj.prediction(clf,test_fp,res_fp)
	




	
