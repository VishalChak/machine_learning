
# coding: utf-8



import numpy as np
from sklearn import preprocessing


#Sample data
data =  np.array([[ 1., -1.,  2.], [ 2.,  0.,  0.], [ 0.,  1., -1.]])
print data



#Scaling
data_scaled = preprocessing.scale(data)
print data_scaled
print data_scaled.mean(axis=0)
print data_scaled.std(axis=0)




#Creating scaler instance
scaler = preprocessing.StandardScaler().fit(data)



print scaler
print scaler.mean_                                      
print scaler.scale_                                       

scaler.transform(data) 




scaler.transform([[-1.,  1., 0.]]) #New element


# It is possible to disable either centering or scaling by either passing with_mean=False or with_std=False to the constructor of StandardScaler.


#Scaling features to a range
min_max_scaler = preprocessing.MinMaxScaler()
data_train_minmax = min_max_scaler.fit_transform(data)
data_train_minmax




data_test = np.array([[ -3., -1.,  4.]]) #New instance
data_test_minmax = min_max_scaler.transform(data_test)
data_test_minmax


# MaxAbsScaler works in a very similar fashion, but scales in a way that the training data lies within the range [-1, 1] by dividing through the largest maximum value in each feature. It is meant for data that is already centered at zero or sparse data. 



#MaxAbsScaler 
max_abs_scaler = preprocessing.MaxAbsScaler()
data_train_maxabs = max_abs_scaler.fit_transform(data)
print data_train_maxabs                # doctest +NORMALIZE_WHITESPACE^
data_test = np.array([[ -3., -1.,  4.]])
data_test_maxabs = max_abs_scaler.transform(data_test)
print data_test_maxabs                 

max_abs_scaler.scale_         




#Normalization (Dot product or Matrices)
X = [[ 1., -1.,  2.], [ 2.,  0.,  0.],[ 0.,  1., -1.]]
X_normalized = preprocessing.normalize(X, norm='l2')

X_normalized 




from sklearn.preprocessing import Normalizer
normalizer = preprocessing.Normalizer().fit(X)  # fit does nothing
normalizer



normalizer.transform(X)



#Feature binarization
X = [[ 1., -1.,  2.],[ 2.,  0.,  0.],[ 0.,  1., -1.]]
print X
binarizer = preprocessing.Binarizer().fit(X)  # fit does nothing
print binarizer

binarizer.transform(X)




#Adjust Threshold
binarizer = preprocessing.Binarizer(threshold=1.1)
binarizer.transform(X)




#Imputation of missing values
import numpy as np
from sklearn.preprocessing import Imputer
imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
imp.fit([[1, 2], [np.nan, 3], [7, 6]])
Imputer(axis=0, copy=True, missing_values='NaN', strategy='mean', verbose=0)
X = [[np.nan, 2], [6, np.nan], [7, 6]]
print(imp.transform(X))    




#Custom Transformation
import numpy as np
from sklearn.preprocessing import FunctionTransformer
transformer = FunctionTransformer(np.log1p)
X = np.array([[0, 1], [2, 3]])
transformer.transform(X)




