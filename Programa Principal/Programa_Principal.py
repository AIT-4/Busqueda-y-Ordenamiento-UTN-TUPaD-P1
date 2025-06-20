import csv
import time # Para medir el tiempo
import os

lista_patentes = []

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'patentes.csv')

# Se abre el archivo utilizando la ruta construida.
with open(csv_path, 'r', newline='') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        lista_patentes.append(fila)

# El archivo patentes.csv tiene 100.000 elementos (patentes) con sus datos correspondientes del automovil.

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        # Las comparaciones <= y > funcionan lexicográficamente con cadenas
        less = [x for x in lista[1:] if x['patente'] <= pivot['patente']]
        greater = [x for x in lista[1:] if x['patente'] > pivot['patente']]
        return quicksort(less) + [pivot] + quicksort(greater)

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        patente_actual = lista[medio]['patente']
        if patente_actual == objetivo:
            return lista[medio]
        elif patente_actual < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def mostrar_vehiculo(vehiculo):
    print(f"El automóvil patente {vehiculo['patente']}, marca {vehiculo['marca']}, "
            f"modelo {vehiculo['modelo']}, año {vehiculo['anio']}, color {vehiculo.get('color', 'desconocido')} "
            f"se encuentra en la base de datos.")

print("--- Ordenamiento con Quicksort de patentes en lista ---")
print("Primeros 3 vehículos sin ordenar:")
for v in lista_patentes[:3]:
    mostrar_vehiculo(v)

# Se ordena la lista
inicio_tiempo_quicksort = time.time() # Comienza a medir tiempo
lista_patentes_ordenada = quicksort(lista_patentes) 
fin_tiempo_quicksort = time.time() # Termina contador

print("Primeros 3 vehículos ordenados por patente:")
for v in lista_patentes_ordenada[:3]:
    mostrar_vehiculo(v)

print(f"---Tiempo de ordenamiento: {(fin_tiempo_quicksort - inicio_tiempo_quicksort):.6f} seg---")

print("\n" + "/" * 40 + "\n")

print("---Busqueda BINARIA de patentes en lista.---")
print("Ejemplo: NYG296 o PNZ619")
patente = input("Ingrese la patente interesada en buscar: ")

inicio_lineal = time.time() # Comienza a medir tiempo
resultado = busqueda_binaria(lista_patentes_ordenada, patente)
if resultado != -1:
    mostrar_vehiculo(resultado)
else:
    print("Patente no encontrada.")

fin_lineal = time.time() # Termina contador
print(f"---Tiempo de busqueda: {(fin_lineal - inicio_lineal):.6f} seg---")