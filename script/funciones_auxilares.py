#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 13:46:59 2020

@author: egidio

funciones extendidas para la consola
"""

from termcolor import colored
from colorama import Fore, Style
import pandas as pd

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

print(bcolors.WARNING + "Módulo importado de colores" + bcolors.ENDC)


def pcolor(string, tipo=None):
    TS = pd.Timestamp.now().strftime('%H:%M:%S')
    TS = '[' + TS + ']: '
    if    tipo == 'HEADER':
        mensaje = str(bcolors.HEADER +  TS + str(string) + bcolors.ENDC)
    elif  tipo == 'OK':
        mensaje = str(bcolors.OKBLUE +  TS + str(string) + bcolors.ENDC)
    elif  tipo == 'INFO':
        mensaje = str(bcolors.OKGREEN +  TS + str(string) + bcolors.ENDC)
    elif  tipo == 'WARNING':
        mensaje = str(bcolors.WARNING +  TS + str(string) + bcolors.ENDC)
    elif  tipo == 'FAIL':
        mensaje = str(bcolors.FAIL +  TS + str(string) + bcolors.ENDC)
    else:
        mensaje = str(bcolors.WARNING +  TS + str(string) + bcolors.ENDC)
        
    return print(mensaje)

def salto_color(tipo=None):
    
    string = '======================================================'

    TS = pd.Timestamp.now().strftime('%H:%M:%S')
    TS = '[' + TS + ']: '
    if    tipo == 'HEADER':
        mensaje = str(bcolors.HEADER +  TS + str(string) + bcolors.ENDC)
    elif  tipo == 'OK':
        mensaje = str(bcolors.OKBLUE +  TS + str(string) + bcolors.ENDC)
    elif  tipo == 'INFO':
        mensaje = str(bcolors.OKGREEN +  TS + str(string) + bcolors.ENDC)
    elif  tipo == 'WARNING':
        mensaje = str(bcolors.WARNING +  TS + str(string) + bcolors.ENDC)
    elif  tipo == 'FAIL':
        mensaje = str(bcolors.FAIL +  TS + str(string) + bcolors.ENDC)
    else:
        mensaje = str(bcolors.WARNING +  TS + str(string) + bcolors.ENDC)
        
    return print(mensaje,), print(mensaje,), print(mensaje,)