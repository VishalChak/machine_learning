#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 18:55:16 2017

@author: vishal
"""

folder = "identify_digits/"
base_path  = "/home/vishal/ML/AV/"
data_path = base_path+"DataSet/"+folder

img_train_dir = data_path+"Train/Images/train/"
img_test_dir = data_path+"Train/Images/test/"

label_path = data_path+"Train/train.csv"

from tqdm import tqdm
import os
import pandas as pd
import cv2
import numpy as np
import tensorflow as tf
import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.estimator import regression


import matplotlib
matplotlib.matplotlib_fname()
import matplotlib.pyplot as plt


label_data = pd.read_csv(label_path)

label_list = label_data['label']
label_list.index = label_data['filename']


LR = 1e-3
MODEL_NAME = 'digit'
IMG_SIZE = 50

def create_label(img):
    label = label_list[img]
    if label == 0 :
        return np.array([1,0,0,0,0,0,0,0,0,0])
    elif label ==1:
        return np.array([0,1,0,0,0,0,0,0,0,0])
    elif label ==2:
        return np.array([0,0,1,0,0,0,0,0,0,0])
    elif label ==3:
        return np.array([0,0,0,1,0,0,0,0,0,0])
    elif label ==4:
        return np.array([0,0,0,0,1,0,0,0,0,0])
    elif label ==5:
        return np.array([0,0,0,0,0,1,0,0,0,0])
    elif label ==6:
        return np.array([0,0,0,0,0,0,1,0,0,0])
    elif label ==7:
        return np.array([0,0,0,0,0,0,0,1,0,0])
    elif label ==8:
        return np.array([0,0,0,0,0,0,0,0,1,0])
    elif label ==9:
        return np.array([0,0,0,0,0,0,0,0,0,1])


def create_traing_data():
    training_data = []    
    for img in tqdm(os.listdir(img_train_dir)):
        path  = os.path.join(img_train_dir, img)
        img_data = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        img_data = cv2.resize(img_data, (IMG_SIZE, IMG_SIZE))
        training_data.append([np.array(img_data),create_label(img)])
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

    convnet = fully_connected(convnet, 10, activation = 'softmax')
    convnet = regression(convnet, optimizer = 'adam', learning_rate = LR, loss = 'categorical_crossentropy', name = 'target')

    model_big = tflearn.DNN(convnet, tensorboard_dir='log', tensorboard_verbose=0)
    model_big.fit(X_train,y_train, n_epoch=10, validation_set=(X_test, y_test), snapshot_step=500, show_metric=True, run_id=MODEL_NAME)
    return model_big

data = create_traing_data()
X_train, y_train, X_test, y_test = train_test_split(data)

model = create_model_bigger(X_train, y_train)

model

def create_test_data():
    test_data = []
    for img in tqdm(os.listdir(img_test_dir)): 
        path = os.path.join(img_test_dir,img)
        IMG_NUM = img.split('.')[0]
        img_data = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        img_data = cv2.resize(img_data, (IMG_SIZE, IMG_SIZE))
        test_data.append([np.array(img_data), IMG_NUM])
    return test_data

test_data = create_test_data()

test_list = []

for img_data, img_num in test_data:
    data = img_data.reshape(IMG_SIZE, IMG_SIZE, 1)
    pred = model.predict([data])
    test_list.append([img_data, img_num,np.argmax(pred)])

img_num_list = []
pred_list = []
for img, img_num, pred in test_list:
    img_num_list.append(img_num)
    pred_list.append(pred)
    print(img_num, pred)

test_list[0]
res_data = pd.DataFrame()
res_data['filename'] = img_num_list
res_data['label'] = pred_list

res_data.head()
res_data.to_csv(data_path+"prediction.csv", index= False)

'''img_data, num, pred = test_list[4]

data = img_data.reshape(IMG_SIZE, IMG_SIZE, 1)

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111)
ax.imshow(img_data, cmap="gray")
plt.show()
print(pred)'''

img_5_data = cv2.imread("/home/vishal/ML/Kaggle/Digit_Recognizer/Data/five.jpg", cv2.IMREAD_GRAYSCALE)
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111)
ax.imshow(img_5_data, cmap="gray")

img_5_data = cv2.resize(img_5_data, (IMG_SIZE, IMG_SIZE))
img_5_data = img_5_data.reshape(IMG_SIZE, IMG_SIZE, 1)

pred_5 = model.predict([img_5_data])

print(np.argmax(pred_5))


kgg_path = "/home/vishal/ML/Kaggle/Digit_Recognizer/Data/test.csv"

kgg_data = pd.read_csv(kgg_path)

kgg_list = kgg_data.values.tolist()

kgg_test = []
for img_data in kgg_list:
    print(img_data)


fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111)
ax.imshow(kgg_list[0], cmap="gray")
