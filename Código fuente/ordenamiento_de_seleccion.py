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
# Búsqueda por Selección

# Definimos la función de Ordenamiento por Selección
def ordenamiento_seleccion(lista):
    largo = len(lista) # Obtiene el número total de elementos en la lista
    # Bucle exterior: recorre la lista para colocar cada elemento en su posición final
    for i in range(largo):
        # Asume que el elemento actual es el mínimo en la parte no ordenada
        min_index = i 
        # Bucle interior: busca el elemento mínimo en la parte restante de la lista (no ordenada)
        for j in range(i + 1, largo):
            if lista[j] < lista[min_index]:
                min_index = j # Actualiza el índice si encuentra un elemento más pequeño
        # Intercambia el elemento mínimo encontrado con el elemento en la posición actual 'i'
        lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista # Devuelve la lista ya ordenada

# --- Programa principal ---

lista_ordenada = [] # Lista que contendrá las patentes una vez ordenadas

print("---Ordenamiento por SELECCION de patentes en lista.---")
print("Primeros 10 items sin ordenar.")
print(lista_patentes[:10]) # Muestra los primeros 10 elementos de la lista original (sin ordenar)

inicio_tiempo = time.time() # Comienza a medir el tiempo justo antes de iniciar el ordenamiento
lista_ordenada = ordenamiento_seleccion(lista_patentes) # Llama a la función de ordenamiento por selección
fin_tiempo = time.time() # Termina de medir el tiempo después de que el ordenamiento finaliza

print("Primeros 10 items ordenados.")
print(lista_ordenada[:10]) # Muestra los primeros 10 elementos de la lista ya ordenada

# Muestra el tiempo total que tomó el ordenamiento por selección, formateado a 6 decimales
print(f"---Tiempo de busqueda: {(fin_tiempo - inicio_tiempo):.6f} seg---")
# Se realizo prueba y el tiempo fue de 174.304 seg (2 minutos y medio aproximadamente)