# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 10:42:58 2021

@author: Oyelade
"""
from utils.MeasureUtil import MeasureOutput
from utils.IOUtil import _save_results_to_csv__, _save_solutions_to_csv__ 
from utils.GraphUtil import _draw_rates__
import numpy as np


class ProcessResult:
	
    def __init__(self, params=None, model_params=None):
        self.obj_func = params["obj_func"]
        self.total_time_train = params["total_time_train"]
        self.time_system = params["time_system"]
        self.meta_name = model_params["meta_name"]
        self.f_sn = model_params["f_sn"]
        self.meta_name = model_params["meta_name"]
        self.pop_size = model_params["pop_size"]
        self.epoch = model_params["epoch"]
        self.log_filename='result_'+str(model_params["run"])
        self.global_log_filename='models_result_'+str(model_params["run"])
        self.path_save_result=params["path_save_result"]
        self.minv=params["min_val"]
        
    def _save_results__(self, solutions=None, gbest=None, infec=[], recov=[], death=[], hosp=[], vaccin=[], suscep=[], quarantine=[]):
            
            measure = MeasureOutput(solutions, self.minv, gbest, number_rounding=4)
            measure._fit__()
                  
            model_based_result = {
                    'model_name': self.meta_name,
                    'f_sn':self.f_sn,
                    'obj_func': self.obj_func, 
                    'total_time_train': self.total_time_train, 
                    'time_system': self.time_system,
                    'gbest': gbest,
    		        'infection': len(infec), 
                    'recovery': len(recov), 
                    'death': len(death), 
                    'hospitalization': len(hosp), 
                    'vaccination': len(vaccin), 
                    'quarantine': len(quarantine)
    		        }
            
            obj_func_based_result = {
                    'model_name': self.meta_name, 
                    'f_sn':self.f_sn,
                    'obj_func': self.obj_func, 
                    'best': measure.best, 
                    'mean': measure.mean, 
                    'std': measure.std, 
                    'worst': measure.worst,
                    'avg': measure.avg,
                    'median': measure.median,
                    'deviation': measure.deviation,
                    'min': self.minv,
    		        }
            
            solution = {
                    'model_name': self.meta_name, 
                    'f_sn':self.f_sn,
                    'obj_func': self.obj_func, 
                    'solution': solutions,
                    }
            
            _save_solutions_to_csv__(solution, self.log_filename, self.path_save_result + "solutions/")
            _save_results_to_csv__(solution, self.global_log_filename, self.path_save_result+ "solutions/all/")
            _save_results_to_csv__(model_based_result, self.global_log_filename, self.path_save_result+ "models/")
            _save_results_to_csv__(obj_func_based_result, self.log_filename, self.path_save_result+ "objfunc/")
            '''
            if isinstance(gbest, int) or isinstance(gbest, float):
                print('Best Solutions: '+str(gbest))
            else:
                print('Best Solutions: '+str(np.stack(gbest)))
            '''   
            print('best: %f, mean: %f, std: %f, worst: %f, median: %f, average: %f, deviation: %f' % (measure.best, measure.mean, measure.std, measure.worst, measure.median, measure.avg, measure.deviation))
            
            return measure.best,measure.mean,measure.std,measure.worst,measure.avg,measure.median,measure.deviation, gbest, self.time_system, self.total_time_train        
            
    def _draw_results__(self, infec=[], recov=[], death=[], hosp=[], vaccin=[], suscep=[], quarantine=[]):
        data =[]
        data.append([infec, 'I'])
        data.append([recov, 'R'])
        data.append([death, 'D'])
        data.append([hosp, 'H'])
        data.append([vaccin, 'V'])
        data.append([suscep, 'S'])
        data.append([quarantine, 'Q'])
        _draw_rates__(data,self.log_filename, self.path_save_result+ "graphs/")
        obj_func_based_result = {
                    'model_name': self.meta_name, 
                    'f_sn':self.f_sn,
                    'obj_func': self.obj_func, 
                    'Susceptible': suscep, 
                    'Infection': infec, 
                    'Recovery': recov, 
                    'Death': death, 
                    'Hospitalization': hosp,
                    'Vaccination': vaccin,
                    'Quarantine': quarantine
    		        }
        _save_results_to_csv__(obj_func_based_result, self.log_filename, self.path_save_result+ "graphs/")
        
    def _save_computed_avg_results__(self, runs=1, overall_best=0, overall_mean=0, overall_std=0, overall_worst=0, overall_avg=0, overall_median=0,overall_deviation=0,overall_gbest=0,overall_time_system=0,overall_total_time_train=0):        
        overall_best=overall_best/runs
        overall_mean=overall_mean/runs
        overall_std=overall_std/runs
        overall_worst=overall_worst/runs
        overall_avg=overall_avg/runs
        overall_median=overall_median/runs
        overall_deviation=overall_deviation/runs
        
        overall_gbest=overall_gbest/runs
        overall_time_system=overall_time_system/runs
        overall_total_time_train=overall_total_time_train/runs
        
        obj_func_based_result = {
                    'model_name': self.meta_name, 
                    'f_sn':self.f_sn,
                    'obj_func': self.obj_func, 
                    'best': overall_best, 
                    'mean': overall_mean, 
                    'std': overall_std, 
                    'worst': overall_worst,
                    'avg': overall_avg,
                    'median': overall_median,
                    'deviation': overall_deviation,
                    'min': self.minv,
    		        }
        
        model_based_result = {
                    'model_name': self.meta_name,
                    'f_sn':self.f_sn,
                    'obj_func': self.obj_func, 
                    'total_time_train': overall_total_time_train, 
                    'time_system': overall_time_system,
                    'gbest': overall_gbest,
    		        }
        _save_results_to_csv__(obj_func_based_result, self.log_filename, self.path_save_result+ "summary_metrics/")
        _save_results_to_csv__(model_based_result, self.log_filename, self.path_save_result+ "summary_time/")