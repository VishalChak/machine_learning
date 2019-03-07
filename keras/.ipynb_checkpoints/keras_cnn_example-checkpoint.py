import numpy as np
np.random.seed(123)


from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten

from keras.layers import Conv2D, MaxPooling2D
from keras.utils import np_utils

from keras.datasets import mnist
from keras import backend as K
K.set_image_dim_ordering('tf')

(X_train, y_train), (X_test, y_test) = mnist.load_data()

#print(X_train.shape)

import matplotlib
matplotlib.matplotlib_fname()
from matplotlib import pyplot as plt
plt.imshow(X_train[0])
#plt.show()

X_train = X_train.reshape(X_train.shape[0], 1, 28, 28)
X_test = X_test.reshape(X_test.shape[0], 1, 28, 28)
#print(X_train.shape)

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /=225
X_test /=225


Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)

#print(Y_train.shape)
#print(X_train[:10])

model = Sequential()
#model.add(Convolution2D(32, 3, 3, activation='relu'))
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(1,28,28)))

#model.add(Conv2D(32, 3, 3, activation='relu', input_shape=(1,28,28)))
#print (model.output_shape)

