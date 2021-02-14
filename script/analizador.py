#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 23:39:53 2020

@author: egidio
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 19:33:19 2020

@author: egidio
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import datetime as dt
from funciones_auxilares import pcolor

# máximas columnas en pandas
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)


class Analizador:
    
    def __init__(self):
        pcolor('Importaste la clase Analizador', 'HEADER')
        print('Las funciones son:')
        print('archivo_infome')
        print('asignador_dataset')
        print('rango_alcance')
        print('seccion_k')
        
        self.informe_arch = ''
        self.dset = pd.DataFrame()


    def archivo_infome(self, nombrearchivo=None):
        if nombrearchivo:
            self.informe_arch = '../temp/' + nombrearchivo
        else:
            self.informe_arch = '../temp/Informe.txt'

        print(' ', file=open(self.informe_arch,'w'))
        pcolor('Se crea el archivo:', 'INFO')
        pcolor(self.informe_arch, 'INFO')


    def asignador_dataset(self, dataset):
        self.dset = dataset
        pcolor('Se asigna la base de datos', 'INFO')

    def rango_alcance(self):
        # los tiempos de z17 al z8 los divido según requisito planilla
        db1 = self.dset
        titulo = 'REM 8'
    
        result = 'Este informe abarca desde el {inicio} al {fin}, está basado\
        en la la/las siguientes comunas {comunas} con {cantidad} casos cada \
        una'.format(
            inicio = db1.Fecha.describe()['first'].strftime('%d-%m-%Y'),
            fin = db1.Fecha.describe()['last'].strftime('%d-%m-%Y'),
            comunas = db1.Comuna.value_counts().head().index.values,
            cantidad = db1.Comuna.value_counts().head().values
            )
        espacios = '\n \n'
       
        print(titulo, file=open(self.informe_arch,'a'))
        print(result, file=open(self.informe_arch,'a'))
        print(espacios, file=open(self.informe_arch,'a'))
        pcolor('Cabecera del informe', 'INFO')
        pcolor(result, 'INFO')


    def seccion_k(self):
        db1 = self.dset
        cortado = pd.cut(
                db1.Diff_salida_enellugar.dt.seconds,
                [0, 20, 40, 1000000],
                labels = ['Menos 20 min',  '20 a 40 min',  'Más 40 min']
                )
        result = pd.crosstab(
            db1['Bas_avan'],
            cortado,
            margins=True, margins_name= 'Total', dropna=False)
        result.columns.name = 'Tiempo llegada al lugar'
        result.index.name = 'Tipo Móvil'
        
        titulo = 'Sección K: INTERVENCIONES PRE HOSPITALARIAS (SAMU)'
        texto = 'Se asume que todas las intervenciones críticas son realizadas \
        por móviles avanzados y que las no-críticas por móviles básicos. Esto \
        determina que las casillas de las prestaciones críticas tengan valores \
        de cero para móviles básicos y las prestaciones no-críticas tengan \
        valores cero para móviles avanzados. \n \n'
        espacios = '\n \n'
        
        print(titulo, file=open(self.informe_arch,'a'))
        print(texto, file=open(self.informe_arch,'a'))
        print(result, file=open(self.informe_arch,'a'))
        print(espacios, file=open(self.informe_arch,'a'))   
        pcolor('Calculo y escribo la sección K', 'INFO')
        pcolor(result, 'INFO')


    def seccion_l(self):
        db1 = self.dset
    
        test = db1.loc[db1['Motivo del Llamado'] != 'Traslados']
        result = test.groupby(['Categoría Vehículo', 'Bas_avan' ])['Id'].count()
        result.index.names = ['Categoría Vehículo', 'Tipo móvil']
        
        titulo = ' Sección L:  TRASLADOS PRIMARIOS A UNIDADES DE URGENCIA'
        texto = ' '
        espacios = '\n \n'
    
        print(titulo, file=open(self.informe_arch,'a'))
        print(texto, file=open(self.informe_arch,'a'))
        print(result, file=open(self.informe_arch,'a'))
        print(espacios, file=open(self.informe_arch,'a'))
        pcolor('Calculo y escribo la sección L', 'INFO')
        pcolor(result, 'INFO')


    def seccion_m(self):
        db1 = self.dset
    
        test = db1.loc[db1['Motivo del Llamado'] == 'Traslados']
        result = test.groupby(['Categoría Vehículo', 'Bas_avan' ])['Id'].count()
        result.index.names = ['Categoría Vehículo', 'Tipo móvil']
        result
        
        titulo = ' Sección M: TRASLADO SECUNDARIO (Desde un Establecimiento a Otro)'
        texto = ' '
        espacios = '\n \n'
    
        print(titulo, file=open(self.informe_arch,'a'))
        print(texto, file=open(self.informe_arch,'a'))
        print(result, file=open(self.informe_arch,'a'))
        print(espacios, file=open(self.informe_arch,'a'))   
        pcolor('Calculo y escribo la sección M', 'INFO')
        pcolor(result, 'INFO')

    def seccion_n(self):
        db1 = self.dset
        
        # Parametrizo para las patologías del REM8
        politrauma = [
                'Accidente vehicular o transporte. Atropellos',
                'Caídas graves',
                'Accidente múltiples víctimas (cualquier razón)']
        
        db1['Patol'] = np.nan
        db1.loc[
            db1['Submotivo del Llamado'].isin(politrauma),
            'Patol'] = 'PoliTMT'
        db1.loc[
            db1['Submotivo del Llamado'] == 'Colapso respiratorio o circulatorio. PCR. Asfixia',
                'Patol'] = 'PCR'
        db1.loc[
            db1['Submotivo del Llamado'] == 'Dolor de pecho',
                'Patol'] = 'SCA'
        db1.loc[db1['Patol'].isnull(),
                'Patol'] = 'Otros'
    
        db1['Patol'] = pd.Categorical(
            db1['Patol'],
            categories=['PCR', 'PoliTMT', 'SCA', 'Otros'],
            ordered = True)
    
        # Parametrizo para los sexos del REM8
        db1.loc[db1['Género'] == 'Femenino', 'Género'] = 'Fem'
        db1.loc[db1['Género'] == 'Masculino', 'Género'] = 'Mas'
        
        db1['Género'] = pd.Categorical(
                                        db1['Género'],
                                        categories=['Mas', 'Fem'], 
                                        ordered=True)
        
        # escribo la tabla
        dum1 = pd.cut(db1.Edad, range(0, 90, 5), right=False)  
        db1['Patol'].value_counts(sort= False)
        result0 = pd.crosstab(db1['Patol'],db1['Género']) # total
        
        result1 = pd.crosstab(
                db1['Patol'],
                [dum1, db1['Género']]
                )   # dividida por edad
                    # (tuve que setear las
                    # las columnas maximas
                    # de pandas)
        
        # escribo en el informe
        titulo = ' Sección N: TRASLADO SECUNDARIO (Desde un Establecimiento a Otro)'
        texto = 'Es una tabla larga, por lo que se divide en varios espacios '
        espacios = '\n \n'
        
        print(titulo, file=open(self.informe_arch,'a'))
        print(texto, file=open(self.informe_arch,'a'))
        print(result1, file=open(self.informe_arch,'a'))
        print(espacios, file=open(self.informe_arch,'a')) 
        pcolor('Calculo y escribo la sección N', 'INFO')
        pcolor(result0, 'INFO')

#def split_dataframe(df, chunk_size = 10000): 
#    chunks = list()
#    num_chunks = len(df) // chunk_size + 1
#    for i in range(num_chunks):
#        chunks.append(df[i*chunk_size:(i+1)*chunk_size])
#    return chunks