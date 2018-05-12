from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split

import matplotlib
matplotlib.matplotlib_fname()
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler


#make Synthetic data


X, _ = make_blobs(n_samples=50, centers=5,random_state =4, cluster_std=2)
X_train, X_test = train_test_split(X, random_state=5, test_size=.1)


fig, axes = plt.subplots(1,3,figsize=(13,4)) 
axes[0].scatter(X_train[:, 0], X_train[:, 1],c='b', label="training set", s=60)
axes[0].scatter(X_test[:, 0], X_test[:, 1], marker='^', c='r', label="test set", s=60)
axes[0].legend(loc='upper left')
axes[0].set_title("original data")

# scale the data using MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

#visualize the properly scaled data
axes[1].scatter(X_train_scaled[:, 0], X_train_scaled[:, 1],
c='b', label="training set", s=60)
axes[1].scatter(X_test_scaled[:, 0], X_test_scaled[:, 1], marker='^',
c='r', label="test set", s=60)
axes[1].set_title("scaled data")


# rescale the test set separately, so that test set min is 0 and test set max is 1
# DO NOT DO THIS! For illustration purposes only
test_scaler = MinMaxScaler()
test_scaler.fit(X_test)
X_test_scaled_badly = test_scaler.transform(X_test)
# visualize wrongly scaled data
axes[2].scatter(X_train_scaled[:, 0], X_train_scaled[:, 1],
c='b', label="training set", s=60)
axes[2].scatter(X_test_scaled_badly[:, 0], X_test_scaled_badly[:, 1], marker='^',
c='r', label="test set", s=60)
axes[2].set_title("!DO NOT DO THIS! improperly scaled data")
plt.show()
