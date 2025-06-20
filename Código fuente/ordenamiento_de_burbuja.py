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
# Ordenamiento de burbuja

# Definimos funciones

def ordenamiento_burbuja(lista):
    cantidad_elementos = len(lista)
    for i in range(cantidad_elementos):
        for j in range(0, cantidad_elementos - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Programa principal

lista_ordenada = []

print("---Ordenamiento de BURBUJA de patentes en lista.---")
print("Primeros 10 items sin ordenar.")
print(lista_patentes[:10])

inicio_tiempo = time.time() # Comienza a medir tiempo
lista_ordenada = ordenamiento_burbuja(lista_patentes)
fin_tiempo = time.time() # Termina contador

print("Primeros 10 items ordenados.")
print(lista_ordenada[:10])


print(f"---Tiempo de busqueda: {(fin_tiempo - inicio_tiempo):.6f} seg---")
# Se realizo prueba y el tiempo fue de 405,288 seg (7 minutos aproximadamente)