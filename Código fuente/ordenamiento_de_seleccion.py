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
# Busqueda por selección

# Definimos funciones
def ordenamiento_seleccion(lista):
    largo = len(lista)
    for i in range(largo):
        # Encontrar el índice del elemento mínimo
        min_index = i
        for j in range(i+1, largo):
            if lista[j] < lista[min_index]:
                min_index = j
        # Intercambiar el elemento mínimo con el elemento actual
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista

# Programa principal

lista_ordenada = []

print("---Ordenamiento por SELECCION de patentes en lista.---")
print("Primeros 10 items sin ordenar.")
print(lista_patentes[:10])

inicio_tiempo = time.time() # Comienza a medir tiempo
lista_ordenada = ordenamiento_seleccion(lista_patentes)
fin_tiempo = time.time() # Termina contador

print("Primeros 10 items ordenados.")
print(lista_ordenada[:10])

print(f"---Tiempo de busqueda: {(fin_tiempo - inicio_tiempo):.6f} seg---")
# Se realizo prueba y el tiempo fue de 174.304 seg (2 minutos y medio aproximadamente)