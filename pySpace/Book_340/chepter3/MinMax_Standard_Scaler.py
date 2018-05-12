from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import MinMaxScaler
import numpy as np


from sklearn.svm import SVC

cancer = load_breast_cancer()
X = cancer.data
y = cancer.target 
print(X.shape)
print(y.shape)

X_train,X_test, y_train, y_test = train_test_split(X,y, random_state = 1)
print(X_train.shape)
print(X_test.shape)

scaler = MinMaxScaler()
scaler.fit(X_train)

np.set_printoptions(suppress=True, precision=2)
X_train_scaled = scaler.transform(X_train)

# print data properties before and after scaling
print("Transformation shape : %s" %(X_train_scaled.shape,))
print("pre-feature minimum before scalling:\n %s" % X_train.min(axis = 0))
print("pre-feature maxmum before scalling:\n %s" % X_train.max(axis = 0))

print("pre-feature minimum after scalling:\n %s" % X_train_scaled.min(axis = 0))
print("pre-feature maximum after scalling:\n %s" % X_train_scaled.max(axis = 0))


# transform test data
X_test_scaled = scaler.transform(X_test)
# print test data properties after scaling
print("per-feature minimum after scaling: %s" % X_test_scaled.min(axis=0))
print("per-feature maximum after scaling: %s" % X_test_scaled.max(axis=0))

svm = SVC(C=100)
svm.fit(X_train,y_train)
print(svm.score(X_test,y_test))


scaler = MinMaxScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
# learning an SVM on the scaled training data


svm.fit(X_train_scaled, y_train)
# scoring on the scaled test set
svm.score(X_test_scaled, y_test)

print(svm.score(X_test_scaled, y_test))


# preprocessing using zero mean and unit variance scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
# learning an SVM on the scaled training data
svm.fit(X_train_scaled, y_train)
# scoring on the scaled test set
svm.score(X_test_scaled, y_test)

print(svm.score(X_test_scaled, y_test))
