import csv
import time # Para medir el tiempo

lista_patentes = []
with open('./Busqueda-y-Ordenamiento-UTN-TUPaD-P1/Código fuente/patentes.csv', 'r') as archivo: 
    # IMPORTANTE: El directorio debe ser el absoluto y no el relativo para que encuentre el archivo
    lector = csv.DictReader(archivo)
    for fila in lector:
        lista_patentes.append(fila['patente'])

# El archivo patentes.csv tiene 100.000 elementos (patentes) con sus datos correspondientes del automovil.

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