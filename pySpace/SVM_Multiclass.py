from sklearn import svm

X= [[0],[1],[2],[3]]
y = [0,1,2,3]

clf = svm.SVC(decision_function_shape='ove')
clf.fit(X,y)

print(clf)

dec = clf.decision_function([[1]])
print(dec.shape[1])

from sklearn import svm
X = [[0,0],[2,2]]
y = [0.5,2.5]
clf = svm.SVR()
clf.fit(X,y)

print(clf)
