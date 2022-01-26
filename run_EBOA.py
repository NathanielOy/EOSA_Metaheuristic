from models.multiple_solution.biology_based.EBOA import BaseEBOA
from utils.FunctionUtil import *
from utils.Ucomp import cmp_to_key, ucompare, ureverse
from utils.Settings import *
from time import time
from utils.SavedResult import ProcessResult
from utils.animate_scatter import AnimateScatter

## Setting parameters`
for func_name in func_domain_ranges:
    ranges, obj_func, f_sn, label, min_val=func_domain_ranges[func_name]
    done=['Ackley', 'Brown', 'Sphere','Bent Cigar', 'Composition1', 'Composition2', 'Dixon and Price', 'Discus Function', 
'Fletcher–Powel','Griewank','Generalized Penalized Function 1', 'Generalized Penalized Function 2', 
'Holzman 2 function', 'HGBat','High Conditioned Elliptic Function', 'Hybrid1 Rotated Zakharov Function', 
'Hybrid2: Rotated High Conditioned Elliptic Function','Inverted Cosine Mixture', 'Lévy 3 function', 'Levy', 
'Levy and Montalo', 'Noise', 'Pathological function', 'Perm','Powel', 'Quartic', 'Rastrigin', 'Rotated hyperellipsoid',
'Rosenbrock ','Schwefel 2.26','Schwefel 1.2','Schwefel 2.21','Step','Sum Function','Sum-Power',
'Sum of Different Power',
'SR-F4','SR-F38','SR-F45','SR-F29','SR-F27','Wavy 1','Zakharov','Salmon','Weierstrass Function',] 
    if label not in done:
        continue
    
    overall_best=0
    overall_mean, overall_std=0,0 
    overall_worst, overall_avg, overall_median=0,0,0, 
    overall_deviation=0
    overall_gbest=0
    overall_time_system=0
    overall_total_time_train=0

    for run in range(number_of_runs):
        model_name='EOSA'
        print('Experimenting '+model_name+' ->'+f_sn+' ->'+label+' -> run='+str(run)+' -> '+func_name)
        model_params={"model_name":model_name, 
                      "meta_name":model_name+'_'+str(run), 
                      "f_sn":f_sn,
                      "run":run,
                      "f_name":label,
                      "pop_size":problem_size, 
                      "epoch":epoch
                     }    
        colors = [[1.0, 1.0, 1.0] for _ in range(problem_size)]
        time_system = time()
        
        root_paras = {
            "problem_size": problem_size,
            "domain_range": ranges,
            "print_train": True,
            "objective_func": obj_func,
            "modelrates":modelrates,
        }
        eboa_paras = {
            "epoch": epoch,
            "pop_size": problem_size
        }
    
        ## Run model @include('commons.admin.adminclosemainpage')
        
        md = BaseEBOA(root_algo_paras=root_paras, eboa_paras=eboa_paras, model_rates=modelrates)
        init_sols=md._get_initial_solutions__()
        
        scatter_params={"constraints": ranges,
                        "r":scatter_resolution,
                        "t":scatter_sleep_time,
                        "opt_func": obj_func,
                        "colors":colors, 
                        "solutions":md._unslice_actual_solutions__(init_sols)
                      }
        a_scatter = AnimateScatter(scatter_params,  model_params, label, save_results_dir)
        md._set_scatter__(a_scatter)    
        
        total_time_train = time()
        gbest, solutions=md._train__()
        total_time_train = round(time() - total_time_train, 4)
        a_scatter.save_plot()    
        time_system = round(time() - time_system, 4)
        
        params={"obj_func" : label, 
                "total_time_train":total_time_train, 
                "time_system":time_system, 
                "path_save_result":save_results_dir,
                "min_val":min_val
                }
        
        pr=ProcessResult(params=params, model_params=model_params)
        best, mean, std, worst, avg, median, deviation, gbest, time_system, total_time_train=pr._save_results__(solutions=solutions, gbest=gbest, infec=md.I, recov=md.R, death=md.D, hosp=md.H, vaccin=md.V, suscep=md.S, quarantine=md.Q)
        overall_best+=best
        overall_mean+=mean
        overall_std+=std
        overall_worst+=worst
        overall_avg+=avg
        overall_median+=median 
        overall_deviation+=deviation
        overall_gbest+=gbest
        overall_time_system+=time_system
        overall_total_time_train+=total_time_train
        pr._draw_results__(infec=md.i_epoch, recov=md.r_epoch, death=md.d_epoch, hosp=md.h_epoch, vaccin=md.v_epoch, suscep=md.s_epoch, quarantine=md.q_epoch)
        
    pr._save_computed_avg_results__(number_of_runs, overall_best,overall_mean,overall_std,overall_worst,overall_avg,overall_median,overall_deviation,overall_gbest,overall_time_system,overall_total_time_train)
        
