import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Regession is a type of Supervised learning plm in which the responce is continious
# linear Regression is perticular Machine Learning Model that can be used to solve regression plm
 

class Titanic:
	def csv_reader(self,filePath):
		data = pd.read_csv(filePath, index_col = 0)
		return data
	def feature_selection(self, data):
		feature_cols = ['Pclass','Sex','Age', 'SibSp', 'Parch']
		X = data[feature_cols]
		X.loc[X['Sex'] == 'male', 'Sex'] = 1
		X.loc[X['Sex'] == 'female', 'Sex'] = 0
		X["Age"].fillna(X["Age"].mean(), inplace=True)
		return X
		
	def create_model(self, train_fp):
		data = self.csv_reader(train_fp)
		X = self.feature_selection(data)
		y = data['Survived']
		X_train,X_test,y_train,y_test = train_test_split(X,y,random_state = 1)
		linleg = LinearRegression()
		linleg.fit(X_train,y_train)
		#y_pred = linleg.predict(X_test)
		#y_pred[y_pred >=.5] = 1
		#y_pred[y_pred <.5] = 0
		#y_pred = y_pred.astype(int)
		return linleg
	
	def prediction(self,model, test_fp):
		test_data = self.csv_reader(test_fp) 
		test_X = self.feature_selection(test_data)
		y_pred = model.predict(test_X)
		y_pred[y_pred >=.5] = 1
		y_pred[y_pred <.5] = 0
		y_pred = y_pred.astype(int)
		np.savetxt("/home/vishal/ML/Kaggle_Competition/Titanic/res.csv", y_pred, delimiter=",")
		print(y_pred)
if __name__ == "__main__":
	obj = Titanic()
	train_fp = "/home/vishal/ML/Kaggle_Competition/Titanic/train.csv"
	test_fp = "/home/vishal/ML/Kaggle_Competition/Titanic/test.csv"
	linleg = obj.create_model(train_fp)
	obj.prediction(linleg,test_fp)
