import csv
import time # Para medir el tiempo
import os

lista_patentes = []

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'patentes.csv')

# Se abre el archivo utilizando la ruta construida.
with open(csv_path, 'r') as archivo:
        lector = csv.DictReader(archivo)
        for fila in (lector):
            lista_patentes.append(fila['patente'])

# El archivo patentes.csv tiene 100.000 elementos (patentes) con sus datos correspondientes del automovil.

## ALGORITMOS DE ORDENAMIENTO
# Busqueda por Inserción

# Definimos funciones
def ordenamiento_insercion(lista):
    for i in range(len(lista)):
        key = lista[i]
        j = i-1
        while j >=0 and key < lista[j] :
            lista[j+1] = lista[j]
            j -= 1
    lista[j+1] = key
    
# Programa principal

lista_ordenada = []

print("---Ordenamiento por INCERSIÓN de patentes en lista.---")
print("Primeros 10 items sin ordenar.")
print(lista_patentes[:10])

inicio_tiempo = time.time() # Comienza a medir tiempo
lista_ordenada = ordenamiento_insercion(lista_patentes)
fin_tiempo = time.time() # Termina contador

print("Primeros 10 items ordenados.")
print(lista_ordenada[:10])


print(f"---Tiempo de busqueda: {(fin_tiempo - inicio_tiempo):.6f} seg---")