# -*- coding: utf-8 -*-
"""
Created on Fri May 29 09:14:28 2020

@author: raymond_tsai
"""
import pandas as pd
import matplotlib.pyplot as plt
        
def Plot_csv(Column_x,Column_y,path_input,path_output):
    input_data = pd.read_csv(path_input,
                        index_col=False,
                        names=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
#    print(input_data)
    input_data = input_data.dropna(axis =1)
    input_data = input_data.dropna(axis =0)
#    print(input_data)
    PlotX = input_data.pop(Column_x)
    PlotY = input_data.pop(Column_y)
    PlotX = PlotX.astype('float64')
    PlotY = PlotY.astype('float64')
    PlotX = PlotX.values
    PlotY = PlotY.values
    plt.plot(PlotX, PlotY, linewidth=1)
    plt.xlabel('Current')
    plt.ylabel('Power')
    plt.savefig(path_output)
    plt.close()
    