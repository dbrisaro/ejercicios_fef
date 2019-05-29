"""
Ejercicio 4

Escribí un programa que ordene en carpetas todos los archivos por tipo y fecha de creación

Dani Risaro
Mayo 2019
"""

import os
from datetime import datetime
import shutil

dir_desordenado = '/home/daniu/Documentos/curso_fef/fotos_desordenadas/'     # directorio a ordenar

dir_ordenado = '/home/daniu/Documentos/curso_fef/otos_ordenadas/'

os.mkdir(dir_ordenado)

lista_archivos = os.listdir(dir_desordenado)                       # archivos del dir


for iarchivo in lista_archivos:

    stat = os.stat(dir_desordenado + iarchivo)

    fecha = datetime.fromtimestamp(stat.st_mtime).strftime("%b-%Y")

    if os.path.exists(dir_ordenado + fecha)==False:

        os.mkdir(dir_ordenado + fecha)

        shutil.copy(dir_desordenado + iarchivo, dir_ordenado + fecha)

    else:

        shutil.copy(dir_desordenado + iarchivo, dir_ordenado + fecha)
