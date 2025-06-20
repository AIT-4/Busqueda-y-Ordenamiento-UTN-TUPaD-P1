import csv
import time # Para medir el tiempo

lista_patentes = []
with open('./Busqueda-y-Ordenamiento-UTN-TUPaD-P1/Código fuente/patentes.csv', 'r') as archivo: 
    # IMPORTANTE: El directorio debe ser el absoluto y no el relativo para que encuentre el archivo
    lector = csv.DictReader(archivo)
    for fila in lector:
        lista_patentes.append(fila)

# El archivo patentes.csv tiene 100.000 elementos (patentes) con sus datos correspondientes del automovil.

## ALGORITMOS DE BUSQUEDA
# Busqueda Lineal

# Definimos funciones

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i]['patente'] == objetivo:
            return lista[i]
    return -1

# Programa principal

print("---Busqueda LINEAL de patentes en lista de diccionarios.---")
print("Ejemplo: NYG296 o PNZ619")
patente = input("Ingrese la patente interesada en buscar: ")

inicio_lineal = time.time() # Comienza a medir tiempo
resultado = busqueda_lineal(lista_patentes, patente)
if resultado != -1:
    print(f"El automovil es un {resultado['marca']} modelo {resultado['modelo']} del año {resultado['anio']}")
else:
    print("Patente no encontrada.")

fin_lineal = time.time() # Termina contador
print(f"---Tiempo de busqueda: {(fin_lineal - inicio_lineal):.6f} seg---")