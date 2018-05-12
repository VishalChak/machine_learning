import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from sklearn import model_selection
from pandas.tools.plotting import scatter_matrix
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

matplotlib.matplotlib_fname()

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', "sepal-width", "petal_length","petal-width", "calss"]
dataset = pd.read_csv(url, names = names)

# 1 Data shape
print(dataset.shape)

 # data looks
 
print(dataset.head(5))

# use discrive command

print(dataset.describe())

# class distribution
print(dataset.groupby('calss').size())

# Data Visualization  
# Univariate plot
# box and whisker plots

dataset.plot(kind= 'box', subplots = True, layout= (2,2), sharex= False, sharey= False)

# histogram
dataset.hist()
plt.show()

# Mutivariate Plots
# scatter plot matrice
scatter_matrix(dataset)
plt.show()

# Do data Cleaming , pre Procssin or any this related to data pre processing

#-----------------------------------

#  Evalution some Algo
# create a valide dataset 
# spilte -out Validation dataset

array = dataset.values
X = array[:,0:4]
y = array[:,4]
validation_size = 0.20
seed = 7
X_train, X_test, y_train,y_test = model_selection.train_test_split(X,y, test_size = validation_size, random_state = seed)


scoring = 'accuracy'

# spot Check

modles = []
modles.append(('LR', LogisticRegression()))
modles.append(('KNN', KNeighborsClassifier()))
modles.append(('CART', DecisionTreeClassifier()))
modles.append(('NB', GaussianNB()))
modles.append(('SVM', SVC()))




res = []
names = []

for name, modle in modles:
    kfold = model_selection.KFold(n_splits=10, random_state = seed)
    cv_results = model_selection.cross_val_score(modle, X_train, y_train , cv = kfold, scoring = scoring)
    names.append(name)
    msg = "%s : %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)

fig = plt.figure()
fig.suptitle("Algo Comparission")

ax = fig.add_subplot(111)
plt.boxplot(res)
ax.set_xtricklalels(names)
plt.show()


knn  = KNeighborsClassifier()
knn.fit(X_train, y_train)
pred = knn.predict(X_test)

print(accuracy_score(y_test, pred))
print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))
