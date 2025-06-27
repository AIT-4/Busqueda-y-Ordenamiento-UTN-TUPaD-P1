import csv # Módulo para trabajar con archivos CSV
import time # Módulo para medir el tiempo de ejecución del código
import os # Módulo para interactuar con el sistema operativo (rutas de archivos)

lista_patentes = [] # Lista donde se almacenarán solo las patentes (como cadenas de texto)

script_dir = os.path.dirname(os.path.abspath(__file__)) # Obtiene el directorio actual del script
csv_path = os.path.join(script_dir, 'patentes.csv') # Construye la ruta completa al archivo CSV

# Se abre el archivo utilizando la ruta construida.
with open(csv_path, 'r') as archivo:
    lector = csv.DictReader(archivo) # Crea un lector que trata cada fila como un diccionario
    for fila in lector:
        lista_patentes.append(fila['patente']) # Añade SOLO la patente (el texto de la patente) a la lista

# El archivo patentes.csv tiene 100.000 elementos (patentes) con sus datos correspondientes del automovil.

# Definimos funciones

## ALGORITMOS DE ORDENAMIENTO
# Ordenamiento por Quick Sort

def quicksort(lista):
    # Caso base: Si la lista tiene 0 o 1 elemento, ya está ordenada
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0] # Elige el primer elemento como pivote para la partición
        # Crea dos sublistas: 'less' (elementos menores o iguales al pivote)
        # y 'greater' (elementos mayores al pivote). Las comparaciones funcionan lexicográficamente con cadenas.
        less = [x for x in lista[1:] if x <= pivot]
        greater = [x for x in lista[1:] if x > pivot]
        # Combina recursivamente las sublistas ordenadas con el pivote en el medio
        return quicksort(less) + [pivot] + quicksort(greater)

# --- PROGRAMA PRINCIPAL ---

print("--- Ordenamiento con Quicksort de patentes en lista ---")
print("Primeros 10 items sin ordenar.")
print(lista_patentes[:10]) # Muestra los primeros 10 elementos de la lista original (sin ordenar)

inicio_tiempo_quicksort = time.time() # Comienza a medir el tiempo antes de iniciar el ordenamiento
lista_patentes_ordenada = quicksort(lista_patentes) # Llama a la función quicksort para ordenar la lista
fin_tiempo_quicksort = time.time() # Termina de medir el tiempo después de que el ordenamiento finaliza

print("Primeros 10 items ordenados.")
print(lista_patentes_ordenada[:10]) # Muestra los primeros 10 elementos de la lista ya ordenada
# Muestra el tiempo total que tomó el ordenamiento por Quicksort, formateado a 6 decimales
print(f"---Tiempo de ordenamiento: {(fin_tiempo_quicksort - inicio_tiempo_quicksort):.6f} seg---")
