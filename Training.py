# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:10:38 2020

@author: raymond_tsai
"""

import os
#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import SimpleRNN
from sklearn.utils import shuffle

# Build layers with Keras sequential()
path1 = os.getcwd()
path2 = path1+ '\\' + 'data_train_input.csv'
path3 = path1+ '\\' + 'data_train_target.csv'
path4 = 'C:\\Users\\raymond_tsai\\Documents\\Python_Data\\LASER\\LIV_study\\CX_kink_study\\Test_val_data\\csv\\data_combined'
path5 = path4+ '\\' + 'data_train_input.csv'
path6 = path4+ '\\' + 'data_train_target.csv'

    
train_data_frame = pd.read_csv(path2, header=0, index_col=0)
train_targets_frame = pd.read_csv(path3, header=0, index_col=0)
train_data_frame.insert(0, 'target', train_targets_frame )
train_data_frame = shuffle(train_data_frame)
train_targets_frame = train_data_frame.pop('target')

train_data_frame = train_data_frame.astype('float64')
train_targets_frame = train_targets_frame.astype('float64')
train_data = train_data_frame.values
train_targets = train_targets_frame.values

mean = train_data.mean(axis=0)
train_data -= mean
std = train_data.std(axis=0)
train_data /= std

test_data_frame = pd.read_csv(path5, header=0, index_col=0)
test_targets_frame = pd.read_csv(path6, header=0, index_col=0)
test_data_frame=test_data_frame.astype('float64')
test_targets_frame=test_targets_frame.astype('float64')
test_data=test_data_frame.values
test_targets = test_targets_frame.values

test_data -= mean
test_data /= std 


#def build_model():
#    model = models.Sequential()
#    model.add(layers.Conv1D(256, (3,3), activation='relu', input_shape=(1, 100, )))
#    model.add(layers.MaxPooling1D((2,2)))
#    model.add(layers.Conv1D(128, (3,3), activation='relu'))
#    model.add(layers.MaxPooling1D((2,2)))
#    model.add(layers.Conv1D(64, (3,3), activation='relu'))
#    model.add(layers.MaxPooling1D((2,2)))
#    model.add(layers.Flatten())
#    model.add(layers.Dense(128, activation='relu'))
#    model.add(layers.Dense(64, activation='relu'))
#    model.add(layers.Dense(1, activation='sigmoid'))    
#    model.compile(optimizer = 'rmsprop',
#              loss='categorical_crossentropy',
#              metrics=['acc'])
#    return model
#model = build_model()

#model = build_model()
#model = models.Sequential()
#model.add(layers.Conv1D(32, 5, activation='relu',
#          input_shape=(None, )))
#model.add(layers.MaxPooling1D(3))
#model.add(layers.Conv1D(32, 3, activation='relu'))
#model.add(layers.MaxPooling1D(5))
#model.add(layers.Conv1D(32, 3, activation='relu'))
#model.add(layers.GlobalMaxPooling1D())
#model.add(layers.Dense(1))
train_data=train_data.reshape(train_data.shape[0],train_data.shape[1],1)
test_data=test_data.reshape(test_data.shape[0],test_data.shape[1],1)
model = models.Sequential()
model.add(SimpleRNN(16, return_sequences=True))
model.add(SimpleRNN(8))
model.add(layers.Dense(8, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])           
history = model.fit(train_data, train_targets,
                    epochs=100,
                    batch_size=10,
                    validation_split=0.4)

history_dict = history.history
acc = history_dict['accuracy']
kink_predict = model.predict(test_data)
loss_values = history_dict['loss']
val_loss_values = history_dict['val_loss']
acc_value = history_dict['accuracy']
val_acc_value = history_dict['val_accuracy']
epochs = range(1, len(acc) + 1)
plt.plot(epochs, acc_value, 'bo', label='acc')
plt.plot(epochs, val_acc_value, 'b', label='Validation acc')
plt.title('Training and validation acc')
plt.xlabel('Epochs')
plt.ylabel('acc')
plt.legend()
plt.show()