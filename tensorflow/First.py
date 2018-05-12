#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 17:21:37 2017

@author: vishal
"""
import tensorflow as tf

x = tf.Variable(3,name='x')
y = tf.Variable(4,name = 'y')
f= x*x*y +y +2

session = tf.Session()
session.run(x.initializer)
session.run(y.initializer)

result = session.run(f)
result
session.close()

with tf.Session() as sess:
    x.initializer.run()
    y.initializer.run()
    res = f.eval()

res

init = tf.global_variables_initializer()

with tf.Session() as sess:
    init.run() # actually initialize all the variables
    result = f.eval()
    
sess = tf.InteractiveSession()
init.run()
res = f.eval()
print(res)
sess.close()

#Managing graphs

x1 = tf.Variable(1)

x1.graph is tf.get_default_graph()

graph = tf.Graph()

with graph.as_default():
    x2 = tf.Variable(2)


x2.graph is graph

x2.graph is tf.get_default_graph()

#Lifecycle of a node value 

w = tf.constant(3)
x = w+2
y = x+3
z = x+5

    
    
    
with tf.Session() as sess:
    print(y.eval()) # 10
    print(z.eval()) # 15