from sklearn import svm

X = [[0,1],[1,1]]
y = [0,1]

clf  = svm.SVC()

clf.fit(X,y)
y_predict = clf.predict([[2.,2.]])
print("y_predict :")
print(y_predict)

print("clf.support_vectors_ :")
print(clf.support_vectors_)

print("clf.support_ : ")
print(clf.support_)

print("clf.n_support_:")
print(clf.n_support_)


