"""
Created on Fri Mar  5 10:42:58 2021

@author: Oyelade
"""
from numpy import concatenate, savetxt, array
from csv import DictWriter
from os import getcwd, path, makedirs
from pandas import read_csv


def _save_results_to_csv__(item=None, filename=None, pathsave=None):
    check_directory = getcwd() + "/" + pathsave
    if not path.exists(check_directory):
        makedirs(check_directory)
    with open(pathsave + filename + ".csv", 'a') as file:
        w = DictWriter(file, delimiter=',', lineterminator='\n', fieldnames=item.keys())
        if file.tell() == 0:
            w.writeheader()
        w.writerow(item)

def _save_solutions_to_csv__(solutions=None, filename=None, pathsave=None):
    savetxt(pathsave + filename + ".csv", array(solutions['solution']), delimiter=",")
    return None
