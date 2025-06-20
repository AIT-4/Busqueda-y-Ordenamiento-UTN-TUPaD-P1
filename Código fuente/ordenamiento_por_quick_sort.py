import csv
import time # Para medir el tiempo
import os

lista_patentes = []

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'patentes.csv')

# Se abre el archivo utilizando la ruta construida.
with open(csv_path, 'r') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            lista_patentes.append(fila['patente'])

# El archivo patentes.csv tiene 100.000 elementos (patentes) con sus datos correspondientes del automovil.

# Definimos funciones

## ALGORITMOS DE ORDENAMIENTO
# Ordenamiento por Quick Sort

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        # Las comparaciones <= y > funcionan lexicográficamente con cadenas
        less = [x for x in lista[1:] if x <= pivot]
        greater = [x for x in lista[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

# PROGRAMA PRINCIPAL

print("--- Ordenamiento con Quicksort de patentes en lista ---")
print("Primeros 10 items sin ordenar.")
print(lista_patentes[:10])

inicio_tiempo_quicksort = time.time()
lista_patentes_ordenada = quicksort(lista_patentes)
fin_tiempo_quicksort = time.time()

print("Primeros 10 items ordenados.")
print(lista_patentes_ordenada[:10])
print(f"---Tiempo de ordenamiento: {(fin_tiempo_quicksort - inicio_tiempo_quicksort):.6f} seg---")
