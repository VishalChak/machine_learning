# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 16:20:43 2018

@author: 10638120
"""
import os
from tqdm import tqdm 
import tensorflow as tf
import cv2
import pandas as pd
import numpy as np

import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.estimator import regression

path = "D:\\Vishal\\Dataset\\HE\\dl2\\"
train_path = path +"train_\\"
label_path = path +"train.csv"

data_label = pd.read_csv(label_path)
label_dic = dict(zip(data_label['image_name'], data_label['detected']))

IMG_SIZE = 1024

LR = 1e-3
MODEL_NAME = 'dl2'

def get_label(img):
    cls = label_dic[img]
    if cls == 'class_1':
        return np.array([1,0,0,0,0,0,0,0,0,0,0,0,0,0])
    elif cls == 'class_2':
        return np.array([0,1,0,0,0,0,0,0,0,0,0,0,0,0])
    elif cls == 'class_3':
        return np.array([0,0,1,0,0,0,0,0,0,0,0,0,0,0])
    elif cls == 'class_4':
        return np.array([0,0,0,1,0,0,0,0,0,0,0,0,0,0])
    elif cls == 'class_5':
        return np.array([0,0,0,0,1,0,0,0,0,0,0,0,0,0])
    elif cls == 'class_6':
        return np.array([0,0,0,0,0,1,0,0,0,0,0,0,0,0])
    elif cls == 'class_7':
        return np.array([0,0,0,0,0,0,1,0,0,0,0,0,0,0])
    elif cls == 'class_8':
        return np.array([0,0,0,0,0,0,0,1,0,0,0,0,0,0])
    elif cls == 'class_9':
        return np.array([0,0,0,0,0,0,0,0,1,0,0,0,0,0])
    elif cls == 'class_10':
        return np.array([0,0,0,0,0,0,0,0,0,1,0,0,0,0])
    elif cls == 'class_11':
        return np.array([0,0,0,0,0,0,0,0,0,0,1,0,0,0])
    elif cls == 'class_12':
        return np.array([0,0,0,0,0,0,0,0,0,0,0,1,0,0])
    elif cls == 'class_13':
        return np.array([0,0,0,0,0,0,0,0,0,0,0,0,1,0])
    elif cls == 'class_14':
        return np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,1])
    
            
def create_training_data():
    training_data = []
    for img in tqdm(os.listdir(train_path)):
        img_path = os.path.join(train_path, img)
        img_data = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
        img_data = cv2.resize(img_data, (IMG_SIZE, IMG_SIZE))
        training_data.append([np.array(img_data),get_label(img)])
    return training_data

def train_test_split(train_data):
    train = train_data[:-500]
    test = train_data[-500:]

    X_train = np.array([i[0] for i in train]).reshape(-1, IMG_SIZE, IMG_SIZE,1)
    y_train = [ i[1] for i in train]


    X_test = np.array([i[0] for i in test]).reshape(-1, IMG_SIZE,IMG_SIZE,1)
    y_test = [i[1] for i in test]
    
    return X_train, y_train, X_test, y_test

def create_model_bigger(X_train,y_train):
    tf.reset_default_graph()
    
    convnet = input_data(shape=[None, IMG_SIZE, IMG_SIZE, 1], name ='input')

    convnet = conv_2d(convnet, 32,5, activation = 'relu')
    convnet = max_pool_2d(convnet,5)
    
    convnet = conv_2d(convnet, 64, 5, activation= 'relu')
    convnet = max_pool_2d(convnet, 5)

    convnet = conv_2d(convnet, 128, 5, activation= 'relu')
    convnet = max_pool_2d(convnet, 5)

    convnet = conv_2d(convnet, 64, 5, activation= 'relu')
    convnet = max_pool_2d(convnet, 5)

    convnet = conv_2d(convnet, 32, 5, activation= 'relu')
    convnet = max_pool_2d(convnet, 5)
    
    convnet = fully_connected(convnet, 1024, activation = 'relu')
    convnet = dropout(convnet,0.8) 

    convnet = fully_connected(convnet, 14, activation = 'softmax')
    convnet = regression(convnet, optimizer = 'adam', learning_rate = LR, loss = 'categorical_crossentropy', name = 'target')

    model_big = tflearn.DNN(convnet, tensorboard_dir='log', tensorboard_verbose=0)
    model_big.fit(X_train,y_train, n_epoch=10, validation_set=(X_test, y_test), snapshot_step=500, show_metric=True, run_id=MODEL_NAME)
    return model_big

training_data = create_training_data()
X_train, y_train, X_test, y_test = train_test_split(training_data)

model = create_model_bigger(X_train, y_train)

