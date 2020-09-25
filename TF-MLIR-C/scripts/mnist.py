#!/usr/bin/env python3
#! Copyright 2020 Nod Labs
# Official TF MNIST model for benchmarking
# From: https://github.com/tensorflow/models/blob/master/official/vision/image_classification/mnist_main.py
import tensorflow as tf

class Model(tf.keras.Model):
    def __init__(self):
        super(Model, self).__init__()
        self.conv1 = tf.keras.layers.Conv2D(32, kernel_size=5, padding='same', activation='relu',
                      data_format='channels_last', use_bias=False)
        self.pool1 = tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding='same',
                     data_format='channels_last')
        self.conv2 = tf.keras.layers.Conv2D(32, kernel_size=5, padding='same', activation='relu',
                      data_format='channels_last', use_bias=False)
        self.pool2 = tf.keras.layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding='same',
                     data_format='channels_last')
        self.flatten = tf.keras.layers.Flatten(data_format='channels_last')
        self.dense1 = tf.keras.layers.Dense(1024, activation='relu')
        self.dropout = tf.keras.layers.Dropout(0.4)
        self.dense2 = tf.keras.layers.Dense(10, activation='softmax')

    def call(self, x):
        x = self.conv1(x)
        x = self.pool1(x)
        x = self.conv2(x)
        x = self.pool2(x)
        x = self.flatten(x)
        x = self.dense1(x)
        x = self.dropout(x)
        x = self.dense2(x)
        return x
