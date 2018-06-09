#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 01:56:14 2017

@author: vishal
"""


model.save('/home/vishal/ML/AV/identify_digits/models/tf_99_77/model.tflearn')

# Save _model
saver = tf.train.Saver()
sess = tf.Session()
sess.run(tf.global_variables_initializer())
model_path = '/home/vishal/ML/AV/identify_digits/models/tf_99_84/model'
saver.save(sess,model_path)


# Load _Model
    # create n/w
imp_server = tf.train.import_meta_graph(model_path+".meta") 
saver.restore(sess,tf.train.latest_checkpoint('./'))
    #load model_ perameter

