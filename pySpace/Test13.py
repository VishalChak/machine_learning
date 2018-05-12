import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Regession is a type of Supervised learning plm in which the responce is continious
# linear Regression is perticular Machine Learning Model that can be used to solve regression plm
 

class Test13:
	def csv_reader(self,filePath):
		data = pd.read_csv(filePath, index_col = 0)
		return data
	def X_y_Creation_pandas(self, data):
		feature_cols = ['Pclass','Sex','Age', 'SibSp', 'Parch']
		X = data[feature_cols]
		X.loc[X['Sex'] == 'male', 'Sex'] = 1
		X.loc[X['Sex'] == 'female', 'Sex'] = 0
		X["Age"].fillna(X["Age"].mean(), inplace=True)
		y = data['Survived']
		X_train,X_test,y_train,y_test = train_test_split(X,y,random_state = 1)
		linleg = LinearRegression()
		linleg.fit(X_train,y_train)
		y_pred = linleg.predict(X_test)
		y_pred[y_pred >=.5] = 1
		y_pred[y_pred <.5] = 0
		y_pred = y_pred.astype(int)
		print(y_pred)

if __name__ == "__main__":
	obj = Test13()
	train_fp = "D:\\Python\\Kaggle_Competition\\Titanic\\train.csv"
	advertise_fp = "http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv"
	data = obj.csv_reader(train_fp)
	obj.X_y_Creation_pandas(data)
	#data = obj.csv_reader(train_fp)
	#obj.testDF()