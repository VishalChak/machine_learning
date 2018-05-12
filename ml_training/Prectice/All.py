from sklearn.cross_validation import KFold
from sklearn.linear_model import LinearRegression, Lasso,Ridge, ElasticNet, SGDRegressor
import numpy as np
import pylab as pl

from sklearn.datasets import load_boston

boston = load_boston()
key = boston.keys()
header = boston.feature_names
X = boston.data

X = np.array([np.concatenate((v,[1])) for v in boston.data ])


a= 0.3
for name ,met in [('Liner reg', LinearRegression()), ("Lasso", Lasso(fit_intercept=True, alpha=a)),('Ridge', Ridge(fit_intercept=True, alpha=a)),("Elastic",ElasticNet(fit_intercept=True, alpha=a))]:
    met.fit(X,y)
    p = met.predict(X)
    e = p-y
    total_error = np.dot(e,e)
    rmse_train = np.sqrt(total_error/len(p))
    kf= KFold(len(X), n_folds=10)
    err = 0
    
    for train,test in kf:
        met.fit(X[train],y[train])
        p = met.predict(X[test])
        e = p-y[test]
        err += np.dot(e,e)
    
    
    rese_10cv = np.sqrt(err/len(X))
    print("Method: %s"%name)
    print("RMSE on traibn: %.4f"%rmse_train)
    print('RMSE on 10-fold: %.4f'%rese_10cv)
    print("\n")







