# -*- coding: utf-8 -*-
"""

Este archivo importa la base de datos y ejecuta el compilador
de ella en caso de que sea necesario

"""

import pandas as pd
import os

from funciones_auxilares import pcolor


# ==================================================
# Ante todo leo que exista la base de datos y sugiero
# linkearla.
# ==================================================

BD = pd.DataFrame()

def dbexistentes():
    # dir_propuesto = '../../../BD/BD_compiladas/'
    dir_propuesto = '../'

    pcolor('Estos son los archivos existentes en ', 'INFO')
    pcolor(dir_propuesto, 'INFO')
    pcolor('Son las siguientes:', 'INFO')
    
    datos = []
    for dirname, dirnames, filenames in os.walk(dir_propuesto):
        for filename in filenames:
            datos.append(os.path.join(dirname, filename))
    pcolor(datos, 'OK')
    
    pcolor('Si filtro por reportebase encuentro lo siguiente:', 'INFO')
    dir_propuesto_reportebase = [f for f in datos if 'reportebase' in f] 
    pcolor(dir_propuesto_reportebase, 'OK')
    decide = input('Aceptas? [s/n]') or 's'
    if decide == 's':
        pass
    else:
        dir_propuesto_reportebase = input('Favor escribe directorio:')
    
    return dir_propuesto_reportebase[0]
    
def importo_BD(directorio):
    BD = pd.read_pickle(directorio)
    return BD

# esto es especifico para el REM8
def complejidad_ambulancia(BD):
    BD['Bas_avan'] = BD['Tipo Despachado'] 
    BD.loc[BD['Tipo Despachado'] == 'm1' , 'Bas_avan' ] = 'Básico'
    BD.loc[BD['Tipo Despachado'] == 'm2' , 'Bas_avan' ] = 'Avanzado'
    BD.loc[BD['Tipo Despachado'] == 'm3' , 'Bas_avan' ] = 'Avanzado'
    BD.loc[BD['Tipo Despachado'] == 'x5' , 'Bas_avan' ] = 'Avanzado'
    BD['Bas_avan'] = pd.Categorical(
            BD['Bas_avan'],
            categories=['Básico', 'Avanzado'],
            ordered = True)
    pcolor('Parametrizo complejidad móvil', 'INFO')

def descripcion_BD(BD):
    pcolor('Estas son las columnas', 'INFO')
    pcolor(BD.columns, 'INFO')
    
    pcolor('Descripción del tiempo', 'INFO')
    pcolor('\n', 'INFO')
    pcolor(BD.Fecha.describe(), 'INFO')
    
def main():
    # Propongo las bases de datos
    pcolor('Este script asegura las dependencias', 'HEADER')
    dir_lectura = dbexistentes()
    pcolor('Se utilizará el siguiente drectorio', 'HEADER')
    pcolor(dir_lectura, 'OK')
    
    # asigno las bases de datos (importo)
    db_reportebase = importo_BD(dir_lectura)
    print(db_reportebase.info())
    
    # Creo variable especial para REM8 de complejidad
    complejidad_ambulancia(db_reportebase)

    # Describo a grandes rasgos
    descripcion_BD(db_reportebase)
    global BD 
    BD = db_reportebase.copy()

if __name__ == "__main__":
    main()
    
