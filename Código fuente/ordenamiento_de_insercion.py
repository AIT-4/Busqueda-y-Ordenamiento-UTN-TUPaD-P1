import csv # Módulo para trabajar con archivos CSV
import time # Módulo para medir el tiempo de ejecución del código
import os # Módulo para interactuar con el sistema operativo (rutas de archivos)

lista_patentes = [] # Lista donde se almacenarán solo las patentes (como cadenas de texto)

# Construye la ruta completa al archivo CSV de forma independiente del sistema operativo
script_dir = os.path.dirname(os.path.abspath(__file__)) # Obtiene el directorio actual del script
csv_path = os.path.join(script_dir, 'patentes.csv') # Une el directorio con el nombre del archivo CSV

# Abre y lee el archivo CSV
with open(csv_path, 'r') as archivo:
    lector = csv.DictReader(archivo) # Crea un lector que trata cada fila como un diccionario
    for fila in lector:
        lista_patentes.append(fila['patente']) # Añade SOLO la patente (el texto de la patente) a la lista

# El archivo patentes.csv tiene 100.000 elementos (patentes) con sus datos correspondientes del automovil.

## ALGORITMOS DE ORDENAMIENTO
# Ordenamiento por Inserción

# Definimos la función de Ordenamiento por Inserción
def ordenamiento_insercion(lista):
    # Recorre la lista desde el segundo elemento hasta el final
    for i in range(len(lista)):
        key = lista[i] # 'key' es el elemento actual que queremos insertar en su posición correcta
        j = i - 1 # 'j' es el índice del elemento anterior a 'key'
        
        # Mueve los elementos de lista[0..i-1] que son mayores que 'key'
        # una posición adelante de su posición actual
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j] # Desplaza el elemento grande a la derecha
            j -= 1 # Mueve 'j' hacia la izquierda para seguir comparando
        
        lista[j + 1] = key # Inserta 'key' en su posición correcta
    return lista # Devuelve la lista ya ordenada

# --- Programa principal ---

lista_ordenada = [] # Lista que contendrá las patentes una vez ordenadas

print("---Ordenamiento por INCERSIÓN de patentes en lista.---")
print("Primeros 10 items sin ordenar.")
print(lista_patentes[:10]) # Muestra los primeros 10 elementos de la lista original (sin ordenar)

inicio_tiempo = time.time() # Comienza a medir el tiempo justo antes de iniciar el ordenamiento
lista_ordenada = ordenamiento_insercion(lista_patentes) # Llama a la función de ordenamiento por inserción
fin_tiempo = time.time() # Termina de medir el tiempo después de que el ordenamiento finaliza

print("Primeros 10 items ordenados.")
print(lista_ordenada[:10]) # Muestra los primeros 10 elementos de la lista ya ordenada

# Muestra el tiempo total que tomó el ordenamiento por inserción, formateado a 6 decimales
print(f"---Tiempo de busqueda: {(fin_tiempo - inicio_tiempo):.6f} seg---")
# Se realizo prueba y el tiempo fue de 174,908 seg (3 minutos aproximadamente)