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

## ALGORITMOS DE BUSQUEDA
# Busqueda Binaria

# Definimos funciones

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return lista[medio]
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1
    
# Programa principal

# Se ordenna las patentes
lista_patentes_ordenada = sorted(lista_patentes)

print("---Busqueda BINARIA de patentes en lista.---")
print("Ejemplo: NYG296 o PNZ619")
patente = input("Ingrese la patente interesada en buscar: ")

inicio_lineal = time.time() # Comienza a medir tiempo
resultado = busqueda_binaria(lista_patentes_ordenada, patente)
if resultado != -1:
    print(f"El automovil patente {resultado} se encuentra en la base de datos.")
else:
    print("Patente no encontrada.")

fin_lineal = time.time() # Termina contador
print(f"---Tiempo de busqueda: {(fin_lineal - inicio_lineal):.6f} seg---")