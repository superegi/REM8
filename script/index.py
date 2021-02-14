#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 20:57:40 2020

@author: egidio
"""

import pandas as pd
import numpy as np
import os
import datetime as dt
from funciones_auxilares import pcolor, salto_color

from importador import Importador
from analizador import Analizador
from fecha_lugar import Submuestra

# máximas columnas en pandas

pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 50)


def main():
    global consigo_dataset
#    global submuestra
    global escribo_informe
    print('Inicio script')
    
    consigo_dataset = Importador()
    consigo_dataset.dbexistentes()
    consigo_dataset.importo_BD()
    consigo_dataset.complejidad_ambulancia()
    consigo_dataset.descripcion_BD()
    
    # submuestra
    sub = Submuestra()
    sub.asignador_BD(consigo_dataset.BD)
    sub.limites()
    sub.base_ambulancia('Quilpué')
    sub.cortar()
    
    escribo_informe = Analizador()
    escribo_informe.asignador_dataset(sub.BD)
    escribo_informe.archivo_infome(nombrearchivo = 'REM8 Quilpué.txt')
    escribo_informe.rango_alcance()
    escribo_informe.seccion_k()
    escribo_informe.seccion_l()
    escribo_informe.seccion_m()
    escribo_informe.seccion_n()

    sub = Submuestra()
    sub.asignador_BD(consigo_dataset.BD)
    sub.limites()
    sub.base_ambulancia('SAMU')
    sub.cortar()
    
    escribo_informe = Analizador()
    escribo_informe.asignador_dataset(sub.BD)
    escribo_informe.archivo_infome(nombrearchivo = 'REM8 SAMU.txt')
    escribo_informe.rango_alcance()
    escribo_informe.seccion_k()
    escribo_informe.seccion_l()
    escribo_informe.seccion_m()
    escribo_informe.seccion_n()
    
if __name__ == "__main__":
    main()


