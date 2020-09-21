# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 17:33:38 2020

@author: raymond_tsai
"""
import sys,os
import laser_module.data_convert as convert
import laser_module.csv_plot as csplot
sys.path.append("C:\\Users\\raymond_tsai\\Documents\\Python Scripts\\laser")

#path1 = os.getcwd()
path1 = 'C:\\Users\\raymond_tsai\\Documents\\Python Scripts\\laser\\ForTest'
path2 = path1+ '\\' + 'csv'
path3 = path1+ '\\' + 'picture'
if not os.path.isdir(path2):
    os.mkdir(path2)
if not os.path.isdir(path3):
    os.mkdir(path3)
                   
filelist = os.listdir(path1)
for files in filelist:
    filename = os.path.splitext(files)[0]
    filetype = os.path.splitext(files)[1]
    if filetype.lower() == '.dat':
        convert.Convert_dat(files,path1,path2)
        csplot.Plot_csv('a','b',
                        path2 + '\\' + filename+'.csv',
                        path3 + '\\' + filename +'.png')
    elif filetype.lower() == '.xlsx':
        convert.Convert_xlsx(files,path1,path2)
        csplot.Plot_csv('a','c',
                        path2 + '\\' + filename+'.csv',
                        path3 + '\\' + filename +'.png')
    elif filetype.lower() == '.csv':
        convert.Convert_csv(files,path1,path2)
        csplot.Plot_csv('a','b',
                        path2 + '\\' + filename+'.csv',
                        path3 + '\\' + filename +'.png')
