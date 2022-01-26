"""
Created on Fri Mar  5 10:42:58 2021

@author: Oyelade OLAIDE NATHANIEL
"""
import numpy as np
import math
from numpy import round, sqrt, abs, where, mean, asscalar
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score


"""
:param y_true:
:param y_pred:
:param multi_output:    string in [‘raw_values’, ‘uniform_average’, ‘variance_weighted’] or array-like of shape (n_outputs)
:param number_rounding:
"""
class MeasureOutput(object):
    def __init__(self, solutions=None, minv=None, gbest=None, number_rounding=3):
        self.solutions = solutions
        self.gbest = gbest
        self.minv=minv
        self.number_rounding = number_rounding
        self.best, self.mean, self.std, self.worst=None, None, None, None 
        self.std_2, self.mean_2=None, None
        self.avg=None
        self.variance, self.median, self.percentile=None, None, None
        self.deviation=None
        
    def deviation_score(self):
        temp = self.minv -self.best
        self.deviation=temp
        
    def best_score(self):
        temp = np.min(self.solutions)  # 
        self.best=temp
    
    def mean_score(self):
        temp = np.mean(self.solutions)  #self.solutions.np.median(x)
        self.mean=temp
    
    def std_score(self):
        temp = np.std(self.solutions) #
        self.std=temp
    
    def worst_score(self):
        temp = np.max(self.solutions)  # 
        self.worst=temp
    
    def percentile_score(self):
        temp =0 # np.percentile(self.solutions)  # 
        self.percentile=temp
    
    def median_score(self):
        temp = np.median(self.solutions)  # 
        self.median=temp
    
    def avg_score(self):
        temp = np.average(self.solutions)  # 
        self.avg=temp
            
    def variance_score(self):
        temp = np.var(self.solutions)  # 
        self.variance=temp
        
    def cal_mean(self):
        return np.mean(np.array(self.solutions))

    def cal_std(self):
        return np.sqrt(np.mean(np.square(np.array(self.solutions))))

        
    def _fit__(self):
        self.best_score()
        self.mean_score()
        self.std_score()
        self.worst_score()
        self.percentile_score()
        self.median_score()
        self.variance_score()
        self.cal_mean()
        self.cal_std()
        self.avg_score()
        self.deviation_score()
        
    