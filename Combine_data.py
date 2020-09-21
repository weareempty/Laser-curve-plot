# -*- coding: utf-8 -*-
"""
Created on Fri May 29 10:52:20 2020

@author: raymond_tsai
"""

import os
import pandas as pd

path1 = path1 = os.getcwd()
path2 = path1+ '\\' + 'data_combined'
if not os.path.isdir(path2):
    os.mkdir(path2)

filelist = os.listdir(path1)
for i in range(len(filelist)):
    raw_data_path = path1 + '\\' + filelist[i]
    filename = os.path.splitext(filelist[i])[0]
    raw_data_frame = pd.read_csv(raw_data_path, names=['Current', 'Chip power'+str(i+1), 'c', 'd'])
    raw_data_frame = raw_data_frame.drop('d',axis=1)
    raw_data_frame = raw_data_frame.transpose()
    raw_data_frame = raw_data_frame.drop(['Current','c'],axis=0)
    raw_data_frame = raw_data_frame.astype('float64')
    raw_data_frame.to_csv( path2 + '\\' +'data_combined.csv')
    if i == 0 :
        combined_data_frame = raw_data_frame
    else:
        combined_data_frame = combined_data_frame.append(raw_data_frame)
    combined_data_frame.to_csv( path2 + '\\' +'data_combined.csv')

    

