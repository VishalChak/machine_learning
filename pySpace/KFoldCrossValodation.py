from IrisData import *
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib gtk

class KFoldCrossValidation:
	def k_fold_cross_validation(self):
		X,y,z = IrisData.load_iris_data()
		knn = KNeighborsClassifier(n_neighbors = 5)
		score = cross_val_score(knn,X,y,cv = 10, scoring = "accuracy")
		print(score.mean())

	def parameter_tuning(self):
		X,y,z = IrisData.load_iris_data()
		k_scores = []
		k_range = range(1,31)
		for k in k_range:
			knn = KNeighborsClassifier(n_neighbors = k)
			scores = cross_val_score(knn,X,y,cv = 10,scoring = 'accuracy')
			k_scores.append(scores.mean())
		#plt.plot(k_range,k_scores)
		ind = np.arange(1,31)
		ndArr = np.array(k_scores)
		print(ndArr.max())
		print(ndArr[ndArr.max()])
		df = pd.DataFrame(k_scores,ind)
		#print(df)
		
		
		

if __name__ == "__main__":
	obj = KFoldCrossValidation()
	obj.parameter_tuning()
