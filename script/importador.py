#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 18:05:30 2020

@author: egidio
"""

import pandas as pd
import os
from funciones_auxilares import pcolor
        
class Importador:
    
    def __init__(self):
        pcolor('Has importado la clase importadora de BDs', 'HEADER')
        print('Las funciones son:')
        print('dbexistentes')
        print('importo_BD')
        print('complejidad_ambulancia')
        print('descripcion_BD')
        self.dir_propuesto = '../'
        self.directorio = ''
        self.BD = pd.DataFrame()

    def dbexistentes(self):
        # dir_propuesto = '../../../BD/BD_compiladas/'
        
        pcolor('Estos son los archivos existentes en ', 'INFO')
        pcolor(self.dir_propuesto, 'INFO')
        pcolor('Son las siguientes:', 'INFO')
        
        datos = []
        for dirname, dirnames, filenames in os.walk(self.dir_propuesto):
            for filename in filenames:
                datos.append(os.path.join(dirname, filename))
                datos = [ x for x in datos if 'git' not in x ]
                
        pcolor(datos, 'OK')
        
        pcolor('Si filtro por reportebase encuentro lo siguiente:', 'INFO')
        dir_propuesto_reportebase = [f for f in datos if 'reportebase' in f] 
        pcolor(dir_propuesto_reportebase, 'OK')
        decide = input('Aceptas? [s/n]') or 's'
        if decide == 's':
            pass
        else:
            dir_propuesto_reportebase = input('Favor escribe directorio:')
        self.directorio = dir_propuesto_reportebase[0]
        
    def importo_BD(self):
        self.BD = pd.read_pickle(self.directorio)
            
    # esto es especifico para el REM8
    def complejidad_ambulancia(self):
        self.BD['Bas_avan'] = self.BD['Tipo Despachado'] 
        self.BD.loc[self.BD['Tipo Despachado'] == 'm1' , 'Bas_avan' ] = 'Básico'
        self.BD.loc[self.BD['Tipo Despachado'] == 'm2' , 'Bas_avan' ] = 'Avanzado'
        self.BD.loc[self.BD['Tipo Despachado'] == 'm3' , 'Bas_avan' ] = 'Avanzado'
        self.BD.loc[self.BD['Tipo Despachado'] == 'x5' , 'Bas_avan' ] = 'Avanzado'
        self.BD['Bas_avan'] = pd.Categorical(
                self.BD['Bas_avan'],
                categories=['Básico', 'Avanzado'],
                ordered = True)
        pcolor('Parametrizo complejidad móvil', 'INFO')
    
    def descripcion_BD(self):
        pcolor('Estas son las columnas', 'INFO')
        pcolor(self.BD.columns, 'INFO')
        
        pcolor('Descripción del tiempo', 'INFO')
        pcolor('\n', 'INFO')
        pcolor(self.BD.Fecha.describe(), 'INFO')