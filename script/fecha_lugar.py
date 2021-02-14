#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 21:30:36 2020

@author: egidio
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import datetime as dt
from funciones_auxilares import pcolor, salto_color
import calendar


class Submuestra:
    
    def __init__(self):
        pcolor('Inicio de submuestra', 'HEADER')
        self.lim_inferior = np.nan
        self.lim_superior = np.nan
        self.BD = pd.DataFrame()
        
    def asignador_BD(self, dataset):
        self.BD = dataset
        
    def limites(self):
        pcolor('Asumo que el mes a calcular es:', 'INFO')
        pcolor(self.BD.Fecha.describe()['last'].strftime('%m-%Y'), 'INFO')
        decide = input('Aceptas? [s/n]') or 's'

        if decide == 's':
            m = self.BD.Fecha.describe()['last'].month
            y = self.BD.Fecha.describe()['last'].year
            dia_final = calendar.monthrange(y, m)[1]
            
            dum = str(y) + str(m) + str(1)
            dum1 = str(y) + str(m) + str(dia_final)
            
            self.lim_inferior = pd.to_datetime(dum, format='%Y%m%d')
            self.lim_superior = pd.to_datetime(dum1, format='%Y%m%d')
            
        else:
            lee_in = input('Ingresa fecha inical [AAAA-MM-DD]')
            lee_fin = input('Ingresa fecha final [AAAA-MM-DD]')
            self.lim_inferior = pd.to_datetime(lee_in, format='%Y-%m-%d')
            self.lim_superior = pd.to_datetime(lee_fin, format='%Y-%m-%d')

        pcolor('Tu mes listo', 'OK')

    def base_ambulancia(self, base_ambulancia=None):
        pcolor('Hay que elegir la base que se quiere calcular', 'INFO')
        if base_ambulancia:
            if base_ambulancia == 'SAMU':
                pass
            elif base_ambulancia == 'Quilpué':
                sector = self.BD['Nombre Vehículo'].str.contains('R3') == True
                self.BD = self.BD[sector]
        else:
            pcolor('[1] Todo SAMU, [2] Quilpué')
            decide = input('Elige [1/2]')
            if decide == '1':
                pass
            elif decide == '2':
                sector = self.BD['Nombre Vehículo'].str.contains('R3') == True
                self.BD = self.BD[sector]

    def cortar(self):
        pcolor(
            f'Elegiste desde el {self.lim_inferior} al {self.lim_superior},',
            'INFO')
        pcolor(
            f'Elegiste las comunas de {self.BD.Comuna.value_counts().index[0]}',
            'INFO')
        self.BD = self.BD.loc[
                (self.BD.Fecha> self.lim_inferior) &
                (self.BD.Fecha< self.lim_superior)]
        pcolor(self.BD.Fecha.describe(), 'INFO')
        
        

    
