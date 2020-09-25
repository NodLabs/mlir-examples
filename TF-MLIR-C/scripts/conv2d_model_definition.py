#!/usr/bin/env python3
#! Copyright 2020 Nod Labs
import tensorflow as tf

class Model(tf.keras.Model):
    def __init__(self):
        super(Model, self).__init__()
        self.conv2d = tf.keras.layers.Conv2D(32, (3, 3), (1, 1), data_format='channels_last', use_bias=False)

    def call(self, input):
        x = self.conv2d(input)
        x = tf.nn.relu(x)
        y = self.conv2d(input)
        y = tf.nn.relu(y)
        return x + y
