# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 17:59:48 2021

@author: Oyelade
"""
import numpy as np
import random
from scipy.integrate import odeint
import matplotlib.pyplot as plt

class DiffEquation(object):
    
    def __init__(self, diffparams=None, model_rates=None):
        self.epoch = diffparams["epoch"]
        self.S= diffparams["S"]
        self.I= diffparams["I"]
        self.H= diffparams["H"]
        self.R= diffparams["R"]
        self.V= diffparams["V"]
        self.D= diffparams["D"]
        self.PE= diffparams["PE"]
        self.Q= diffparams["Q"]
        self.π=model_rates["recruitment_rate"]
        self.ŋ=model_rates["decay_rate"]
        self.α=model_rates["hospitalization_rate"]
        self.dis=model_rates["disease_induced_death_rate"]
        self.β_1=model_rates["contact_rate_infectious"]
        self.β_2=model_rates["contact_rate_pathogen"]
        self.β_3=model_rates["contact_rate_deceased"]
        self.β_4=model_rates["contact_rate_recovered"]
        self.rr=model_rates["recovery_rate"]
        self.dr=model_rates["natural_death_rate"]
        self.br=model_rates["burial_rate"]
        self.vr=model_rates["vacination_rate"]
        self.hr=model_rates["hospital_treatment_rate"]
        self.vrr=model_rates["vaccination_response_rate"]
        self.qrr=model_rates["quarantine_rate"]
        self.xs=None
        self.ys=None
        
    def _solve_differential__(self, initial_val, func):
        self.xs = np.linspace(0,5, self.epoch)
        
        dy_dx_function=self._fetch_func__(func)
        # sum(initial_val[0]) : equivalent to the summation of the numpy array of the first solution
        # initial_val[1] : represents the fitness value of the solution 
        self.ys = odeint(dy_dx_function, initial_val, # the initial condition
                    self.xs # the values of T: {epoch0, epoch1, epoch2.....epoch_n}
                   )
        self.ys = np.array(self.ys).flatten()
        self.ys=(self.ys - np.min(self.ys)) / (np.max(self.ys) - np.min(self.ys))
        return self.ys
    
    
    def _fetch_func__(self, fname):
        if fname == 'suspectible':
            return self._differential_suspectible__
        elif fname == 'infected':
            return self._differential_infected__
        elif fname == 'hospitalized':
            return self._differential_hospitalized__
        elif fname == 'vaccinated':
            return self._differential_vaccinated__
        elif fname == 'recovery':
            return self._differential_recovery__
        elif fname == 'dead':
            return self._differential_dead__
        elif fname == 'quarantine':
            return self._differential_quarantine__
        
    # Define a function which calculates the derivative of suspectible individuals
    def _differential_suspectible__(self, y, x):
        dif=self.π - (((self.β_1 * len(self.I)) + (self.β_3 * len(self.D)) + (self.β_4 * len(self.R)) + (self.β_2 * len(self.PE)* self.ŋ)) * len(self.S)) -  ((self.dis*len(self.S)) + (self.dr*len(self.I)))                              
        return dif
    
    # Define a function which calculates the derivative of infected individuals
    def _differential_infected__(self, y, x):
        dif=(((self.β_1 * len(self.I)) + (self.β_3 * len(self.D)) + (self.β_4 * len(self.R)) + (self.β_2 * len(self.PE)* self.ŋ)) * len(self.S)) -  ((self.dis*len(self.S)) + ( (self.dr+self.rr) *len(self.I)))                              
        return dif
    
    # Define a function which calculates the derivative  of hospitalized individuals
    def _differential_hospitalized__(self, y, x):
        dif= (self.α *len(self.I)) - (self.rr+self.hr)*len(self.H)                             
        return dif
    
    # Define a function which calculates the derivative  of recovery individuals
    def _differential_recovery__(self, y, x):
        dif= (self.rr *len(self.I)) - self.dis*len(self.R)                             
        return dif
    
    # Define a function which calculates the derivative  of vaccinated individuals
    def _differential_vaccinated__(self, y, x):
        dif= (self.rr *len(self.I)) - (self.vrr+self.vr)*len(self.V)                             
        return dif
    
    # Define a function which calculates the derivative  of dead individuals
    def _differential_dead__(self, y, x):
        dif= (self.dis *len(self.I)) + self.dr*len(self.S) - self.br *len(self.D)                                                         
        return dif
    
    # Define a function which calculates the derivative  of dead individuals
    def _differential_quarantine__(self, y, x):
        dif= (self.π *len(self.I) - (self.rr*len(self.R) +self.dis*len(self.D))) - self.qrr *len(self.Q)                                                         
        return dif
    
    def _plot_differential_equation__(self, label):
        # Plot the numerical solution of our differential equation
        plt.rcParams.update({'font.size': 14})  # increase the font size
        plt.xlabel("x")
        plt.ylabel("y")
        plt.plot(self.xs, self.ys, label=label)
        plt.xlabel('time/epoch')
        plt.ylabel('y(t)')