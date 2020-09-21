# -*- coding: utf-8 -*-
"""
Created on Fri May 29 09:14:28 2020

@author: raymond_tsai
"""
from os import path
import pandas as pd
    
def Convert_dat(file_input,path_input,path_output):
    Olddir = path.join(path_input,file_input)
    filename = path.splitext(file_input)[0]
    filetype = path.splitext(file_input)[1]
    if filetype.lower() == '.dat':
        file_test = open(Olddir,'r')
        Newdir = path.join(path_output, str(filename) + '.csv')
        file_test2 = open(Newdir,'w')
        for lines in file_test.readlines():
            strdata = ",".join(lines.split('\t'))
            file_test2.write(strdata)       
        file_test.close()
        file_test2.close()

def Convert_xlsx(file_input,path_input,path_output):        
    Olddir = path.join(path_input,file_input)
    filename = path.splitext(file_input)[0]
    filetype = path.splitext(file_input)[1]
    if filetype.lower() == '.xlsx':
        file_test = pd.read_excel(Olddir, names = ['a', 'b', 'c', 'd'])
        file_test = file_test.drop([0,1,2,3,4,5,6,7,8,9,10], axis = 0)
        file_test = file_test.astype('float64')
        Newdir = path.join(path_output,str(filename)+ '.csv')
        file_test.to_csv(Newdir, index=False, header = False)
        
def Convert_csv(file_input,path_input,path_output):
    filename = path.splitext(file_input)[0]
    filetype = path.splitext(file_input)[1]
    if filetype.lower() == '.csv':
        Newdir = path.join(path_output,str(filename)+ '.csv')
        file_test = pd.read_csv(path_input + '\\' + file_input,
                                index_col=False,
                                names=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
        file_test = file_test.drop([0,1,2,3], axis = 0)
        file_test = file_test.drop(['g','h'], axis = 1)
        file_test = file_test.dropna(axis =0)
        file_test.to_csv(Newdir, index=False, header = False)
