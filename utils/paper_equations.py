# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 18:00:07 2021

@author: Oyelade
"""
import numpy as np
import random

def get_sub_population(S, PE):    
    I= S[55:]
    Q=[]
    H, V, R, D= I[10:25], I[17:24], I[26:40], I[41:]
    return S, I, H, V, R, D, PE, Q
    
def generate_incubation_period_for_an_individual(max_incubation_period):
    #generate number between 1 and times 2 of the max_incubation_period
    return random.randint(1,max_incubation_period) + (2*max_incubation_period) 

#to update position of individual
def equation1(last_position_at_time_t=None, gbest_pos=None):
    #generates a number between 0.0 - 0.9
    displacement_rate=np.random.rand() 
    #long displacement: displacement_rate > 0.5 eqt (3), otherwise eqt(2)
    movement_rate=equation2_and_3(displacement_rate, gbest_pos)
    p=0.1
    new_pos=last_position_at_time_t+ (p * movement_rate)
    return new_pos, movement_rate
    
def equation2_and_3(displacement_rate, gbest_pos):    
    return (displacement_rate * np.random.rand()) + gbest_pos

def equation6(de, initial_value):
     result=de._solve_differential__(initial_value, 'suspectible')
     #de._plot_differential_equation__('suspectible')
     return result
    
def equation7(de, initial_value):
     result=de._solve_differential__(initial_value, 'infected')
     #de._plot_differential_equation__('infected')
     return result

def equation8(de, initial_value):
     result=de._solve_differential__(initial_value, 'hospitalized')
     #de._plot_differential_equation__('hospitalized')
     return result
    
def equation9(de, initial_value):
     result=de._solve_differential__(initial_value, 'recovery')
     #de._plot_differential_equation__('recovery')
     return result
    
def equation10(de, initial_value):
     result=de._solve_differential__(initial_value, 'vaccinated')
     #de._plot_differential_equation__('vaccinated')
     return result
    
def equation11(de, initial_value):
     result=de._solve_differential__(initial_value, 'dead')
     #de._plot_differential_equation__('dead')
     return result
 
def equation12(de, initial_value):
     result=de._solve_differential__(initial_value, 'quarantine')
     #de._plot_differential_equation__('quarantine')
     return result