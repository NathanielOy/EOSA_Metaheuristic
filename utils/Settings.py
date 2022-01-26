# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 16:50:44 2021

@author: Oyelade
"""

import numpy as np
import random
from utils.FunctionUtil import *


def _unslice_actual_solutions__(pop):
        unsliced_pop=[]
        for p in pop:
            i=p[0]
            unsliced_pop.append(i)
        return unsliced_pop
"""
Constants and values describing rates and variables
"""
'''
Settings from the paper
--------------------------------------------------------------------------------------------
 Notation       Definition                                                     Range of Value
--------------------------------------------------------------------------------------------
    π     Recruitment rate of susceptible human individuals                          Variable
    ŋ    Decay rate of Ebola virus in the environment                               (0, )
    α    Rate of hospitalization of infected individuals                               (0, 1)
        Disease-induced death rate of human individuals                               [0.4, 0.9]
    β1    Contact rate of infectious human individuals                               Variable
    β2    Contact rate of pathogen individuals/environment                           Variable
    β3    Contact rate of deceased human individuals                                   Variable
    β4    Contact rate of recovered human individuals                                   Variable
        Recovery rate of human individuals                                           (0, 1)
        Natural death rate of human individuals                                       (0, 1)
        Rate of  burial of deceased human individuals                               (0, 1)
        Rate of vaccination of individuals                                           (0, 1)
        Rate of response to hospital treatment                                       (0, 1)
        Rate response to vaccination                                               (0, 1)
'''
π=0.1 #Recruitment rate of susceptible human individuals
ŋ=np.random.rand() #Decay rate of Ebola virus in the environment
α=np.random.rand() #Rate of hospitalization of infected individuals
dis=random.uniform(0.4, 0.9)#Disease-induced death rate of human individuals
β_1=0.1#Contact rate of infectious human individuals
β_2=0.1#Contact rate of pathogen individuals/environment
β_3=0.1#Contact rate of deceased human individuals
β_4=0.1#Contact rate of recovered human individuals
rr=np.random.rand() #Recovery rate of human individuals
dr=np.random.rand() #Natural death rate of human individuals
br=np.random.rand() #Rate of  burial of deceased human individuals
vr=np.random.rand() #Rate of vaccination of individuals
hr=np.random.rand() #Rate of response to hospital treatment
vrr=np.random.rand() #Rate response to vaccination
qrr=np.random.rand()	#Rate of quarantine of infected individuals

save_results_dir='./history/results/'

modelrates = {
    "recruitment_rate": π,
    "decay_rate": ŋ,
    "hospitalization_rate": α,
    "disease_induced_death_rate": dis,
    "contact_rate_infectious": β_1,
    "contact_rate_pathogen": β_2,
    "contact_rate_deceased": β_3,
    "contact_rate_recovered": β_4,
    "recovery_rate": rr,
    "natural_death_rate": dr,
    "burial_rate": br,
    "vacination_rate": vr,
    "hospital_treatment_rate": hr,
    "vaccination_response_rate": vrr,
    "quarantine_rate": qrr
}

number_of_runs=1
epoch=1
problem_size=100
scatter_resolution=0.25 #resolution of function meshgrid, default: 0.25
scatter_sleep_time=0.1  #animate sleep time, lower values increase animation speed, default: 0.1')

'''
'Brown', 'Bent Cigar', 'Composition1', 'Composition2', 'Dixon and Price', 'Discus Function', 
'Fletcher–Powel','Griewank','Generalized Penalized Function 1', 'Generalized Penalized Function 2', 
'Holzman 2 function', 'HGBat','High Conditioned Elliptic Function', 'Hybrid1 Rotated Zakharov Function', 
'Hybrid2: Rotated High Conditioned Elliptic Function','Inverted Cosine Mixture', 'Lévy 3 function', 'Levy', 
'Levy and Montalo', 'Noise', 'Pathological function', 'Perm','Powel', 'Quartic', 'Rastrigin', 'Rotated hyperellipsoid',
'Rosenbrock ','Schwefel 2.26','Schwefel 1.2','Schwefel 2.22','Schwefel 2.21','Sphere','Step','Sum Function','Sum-Power',
'Sum of Different Power',
'SR-F4','SR-F38','SR-F45','SR-F29','SR-F27','Wavy 1','Zakharov','Salmon','Weierstrass Function',
'''

benchmark_functions_experiement_2={
    "CEC_5":                           ([-32, 32], CEC_5, 'F1',  'Ackley', 0),   #whale_f10, hho_f10 (Continuous, Non-Differentiable, Separable, Non-Scalable, Multimodal)
    "CEC_EbOA_21":                     ([-10, 10], CEC_EbOA_21, 'F2',  'Alpine', 0), #(Continuous, Non-Differentiable, Separable, Non-Scalable, Multimodal)
    "CEC_EbOA_20":                       ([-1, 4],  CEC_EbOA_20, 'F3',  'Brown', 0),         #  Continuous, Differentiable, Non-Separable, Scalable, Unimodal
    "CEC_2":                           ([-100,100], CEC_2, 'F4',    'Bent Cigar', 0), #F4    Bent Cigar
    "CEC_EbOA_18":                     ([-10, 10], CEC_EbOA_18, 'F5',    'Dixon and Price', 0),         #
    "CEC_3":                           ([-100, 100], CEC_3, 'F6',    'Discus Function', 0),  #
    "CEC_EbOA_14":                        ([-10, 10], CEC_EbOA_14, 'F7',    'Levy', 0),
    "CEC_EbOA_10":                     ([-4, 5], CEC_EbOA_10, 'F8', 'Powel', 0),       
    "CEC_EbOA_9":                      ([-128, 128], CEC_EbOA_9, 'F9',        'Quartic', 0),            
    "whale_f9":                        ([-5.12, 5.12], whale_f9, 'F10',    'Rastrigin', 0),#  hho_f9, CEC_8    
    "C9":                               ([-100,100], C9, 'F11',    'SR-F27', 0),
    "CEC_EbOA_3":                      ([-100,100], CEC_EbOA_3, 'F12',    'Wavy 1', 0),
    "CEC_EbOA_2":                       ([-5, 10], CEC_EbOA_2, 'F13',    'Zakharov', 0),
    "CEC_EbOA_1":                       ([-100, 100], CEC_EbOA_1, 'F14',    'Salmon', 0), 
    "CEC_6":                           ([-0.5, 0.5], CEC_6, 'F15', 'Weierstrass Function', 0) # −0.5 ≤ xi ≤ 0.5
    }
func_domain_ranges = { #represents the constrains of all benchmar functions used in the experimentation
    "C30":                             ([-100, 100], C30, 'F0', 'C30', 0),
    "CEC_5":                           ([-32, 32], CEC_5, 'F1',  'Ackley', 0),   #whale_f10, hho_f10 (Continuous, Non-Differentiable, Separable, Non-Scalable, Multimodal)
    "CEC_EbOA_21":                     ([-10, 10], CEC_EbOA_21, 'F2',  'Alpine', 0), #(Continuous, Non-Differentiable, Separable, Non-Scalable, Multimodal)
    "CEC_EbOA_20":                       ([-1, 4],  CEC_EbOA_20, 'F3',  'Brown', 0),         #  Continuous, Differentiable, Non-Separable, Scalable, Unimodal
    "CEC_2":                           ([-100,100], CEC_2, 'F4',    'Bent Cigar', 0), #F4    Bent Cigar
    "CEC_EbOA_19":                       ([-100,100], CEC_EbOA_19, 'F5',    'Composition1', 0), #F5    Composition1
    "CEC_13":                           ([-100,100], CEC_13, 'F6',     'Composition2', 0), #
    "CEC_EbOA_18":                     ([-10, 10], CEC_EbOA_18, 'F7',    'Dixon and Price', 0),         #
    "CEC_3":                           ([-100, 100], CEC_3, 'F8',    'Discus Function', 0),  #
    "CEC_EbOA_17":                     ([-100, 100], CEC_EbOA_17, 'F9',  'Fletcher–Powel', 0.0001),          #
    "whale_f11":                       ([-600, 600], whale_f11, 'F10',    'Griewank', 0), #  hho_f11, CEC_7
    "hho_f12":                         ([-50, 50], hho_f12, 'F11',        'Generalized Penalized Function 1', 0),  #
    "hho_f13":                         ([-5.12, 5.12], hho_f13, 'F12',        'Generalized Penalized Function 2', 0),  #
    "CEC_EbOA_16":                     ([-100, 100], CEC_EbOA_16, 'F13',        'Holzman 2 function', 0), #
    "CEC_12":                           ([-100,100], CEC_12, 'F14',    'HGBat', 0),
    "CEC_1":                           ([-100,100], CEC_1, 'F15',    'High Conditioned Elliptic Function', 0),
    "gCEC_EbOA_2":                       ([-100,100], gCEC_EbOA_2, 'F16',    'Hybrid1 Rotated Zakharov Function', 0),
    "gCEC_1":                           ([-100,100], gCEC_1, 'F17',    'Hybrid2: Rotated High Conditioned Elliptic Function', 0), 
    "CEC_EbOA_15":                       ([-1,1], CEC_EbOA_15, 'F18',    'Inverted Cosine Mixture', 0),
    "CEC_14":                          ([-10, 10], CEC_14, 'F19',        'Lévy 3 function', 0),
    "CEC_EbOA_14":                        ([-10, 10], CEC_EbOA_14, 'F20',    'Levy', 0),
    "CEC_EbOA_13":                       ([-5, 5], CEC_EbOA_13, 'F21',    'Levy and Montalo', 0),
    "whale_f7":                           ([-1.28, 1.28], whale_f7, 'F22',    'Noise', 0),
    "CEC_EbOA_12":                       ([-100,100],CEC_EbOA_12, 'F23',    'Pathological function', 0),
    "CEC_EbOA_11":                        ([-20, 20], CEC_EbOA_11, 'F24',    'Perm', 0),       
    "CEC_EbOA_10":                     ([-4, 5], CEC_EbOA_10, 'F25', 'Powel', 0),       
    "CEC_EbOA_9":                      ([-128, 128], CEC_EbOA_9, 'F26',        'Quartic', 0),            
    "whale_f9":                        ([-5.12, 5.12], whale_f9, 'F27',    'Rastrigin', 0),#  hho_f9, CEC_8
    "whale_f3":                           ([-100, 100], whale_f3, 'F28',     'Rotated hyperellipsoid', 0),
    "CEC_4":                           ([-30, 30], CEC_4, 'F29',    'Rosenbrock ', 0),#or whale_f5, hho_f5
    "whale_f8":                        ([-500, 500], whale_f8, 'F30',    'Schwefel 2.26', -418.983),  #hho_f8, CEC_9, CEC_10
    "hho_f3":                          ([-100, 100], hho_f3, 'F31',    'Schwefel 1.2', 0), #hho_f3
    "hho_f2":                          ([-100, 100], hho_f2, 'F32',    'Schwefel 2.22', 0), #whale_f2
    "hho_f4":                          ([-100, 100],  hho_f4, 'F33',    'Schwefel 2.21', 0),
    "hho_f1":                            ([-100, 100],  hho_f1, 'F34',    'Sphere', 0),
    "whale_f6":                           ([-100, 100], whale_f6, 'F35',    'Step', 0),  #hho_f6
    "CEC_EbOA_8":                       ([-10, 10], CEC_EbOA_8, 'F36',    'Sum Function', 0),
    "CEC_EbOA_7":                       ([-1, 1], CEC_EbOA_7, 'F37',    'Sum-Power', 0),
    "CEC_EbOA_5":                       ([-100,100], CEC_EbOA_5, 'F38',    'Sum of Different Power', 0),
    "C2":                                ([-100,100], C2, 'F39',    'SR-F4', 0),
    "CEC_EbOA_6":                       ([-100,100], CEC_EbOA_6, 'F40',    'SR-F38', 0),
    "CEC_EbOA_4":                       ([-100,100], CEC_EbOA_4, 'F41',    'SR-F45', 0),
    "C4":                               ([-100,100], C4, 'F42',    'SR-F29', 0),
    "C9":                               ([-100,100], C9, 'F43',    'SR-F27', 0),
    "CEC_EbOA_3":                      ([-100,100], CEC_EbOA_3, 'F44',    'Wavy 1', 0),
    "CEC_EbOA_2":                       ([-5, 10], CEC_EbOA_2, 'F45',    'Zakharov', 0),
    "CEC_EbOA_1":                       ([-100, 100], CEC_EbOA_1, 'F46',    'Salmon', 0), 
    "CEC_6":                           ([-0.5, 0.5], CEC_6, 'F48', 'Weierstrass Function', 0) # −0.5 ≤ xi ≤ 0.5
}

    
'''
https://towardsdatascience.com/optimization-eye-pleasure-78-benchmark-test-functions-for-single-objective-optimization-92e7ed1d1f12
'''