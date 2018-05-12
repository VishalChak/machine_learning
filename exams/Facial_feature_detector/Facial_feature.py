import cv2

from keras.models import Sequential
from keras.layers import normalization , Activation,Dense, GlobalAveragePooling2D

from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.callbacks import ModelCheckpoint

def facial_detection():
    model = Sequential()
    model.add(normalization.BatchNormalization(input_shape=(96, 96, 1)))
    model.add(Convolution2D(24, 5, 5, border_mode='same', init='he_normal',
                            input_shape=(96, 96, 1), dim_ordering='tf'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2), border_mode='valid'))
    
    
    model.add(Convolution2D(36, 5, 5))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2), border_mode='valid'))
    
    model.add(Convolution2D(48, 5, 5))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2), border_mode='valid'))
    
    model.add(Convolution2D(64, 3, 3))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2), border_mode='valid'))
    
    model.add(Convolution2D(64, 3, 3))
    model.add(Activation('relu'))
    
    model.add(GlobalAveragePooling2D());
    
    model.add(Dense(500, activation='relu'))
    model.add(Dense(90, activation='relu'))
    model.add(Dense(30))
    model.compile(optimizer='rmsprop', loss='mse', metrics=['accuracy'])
    checkpointer = ModelCheckpoint(filepath='face_model.h5', verbose=1, save_best_only=True)
    epochs = 30
    #hist = model.fit(X_train, y_train, validation_split=0.2, shuffle=True, epochs=epochs, batch_size=20, callbacks=[checkpointer], verbose=1)
    #features = model.predict(region, batch_size=1)
    

import pandas as pd
if __name__ == "__main__":
    train_path = "/home/vishal/ML/DataScience/UseCases/Facial_feature_detector/training.csv"
    data = pd.read_csv(train_path)
    data.head()