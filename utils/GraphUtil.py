"""
Created on Fri Mar  5 10:42:58 2021

@author: Oyelade
"""
import matplotlib.pyplot as plt
import numpy as np

def _draw_rates__(data=None, filename=None, pathsave=None):
    for d in data:
        x = np.arange(len(d[0]))
        print(d[1]+'   '+str(d[0]))
        plt.plot(x, d[0], label=d[1])       # e.g infection rate
    
    plt.ylabel('Population')
    plt.xlabel('Epoch')
    plt.legend(loc='upper right')
    plt.savefig(pathsave + filename + ".png")
    plt.close()
    return None

def draw_raw_time_series_data_and_show(data=None, label=None, title=None):
    plt.plot(data)
    plt.xlabel(label["y"])
    plt.ylabel(label["x"])
    plt.title(title, fontsize=8)
    plt.show()
    return None


