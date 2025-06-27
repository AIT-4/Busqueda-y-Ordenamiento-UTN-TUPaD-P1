import csv # Módulo para trabajar con archivos CSV
import time # Módulo para medir el tiempo de ejecución
import os # Módulo para interactuar con el sistema operativo y rutas

lista_patentes = [] # Lista donde se almacenarán solo las patentes (como cadenas de texto)

# Construye la ruta completa al archivo CSV para que funcione en cualquier sistema operativo
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'patentes.csv')

# Abre y lee el archivo CSV
with open(csv_path, 'r') as archivo:
    lector = csv.DictReader(archivo) # Crea un lector que trata cada fila como un diccionario
    for fila in lector:
        lista_patentes.append(fila['patente']) # Añade SOLO la patente (el texto de la patente) a la lista

# El archivo patentes.csv tiene 100.000 patentes con sus datos correspondientes.

## ALGORITMOS DE BUSQUEDA

# Función de Búsqueda Binaria
def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1 # Define los límites iniciales de la búsqueda en la lista
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2 # Calcula el índice del elemento central
        if lista[medio] == objetivo:
            return lista[medio] # Si el elemento del medio es el objetivo, lo encuentra y lo devuelve
        elif lista[medio] < objetivo:
            izquierda = medio + 1 # Si el objetivo es mayor, busca en la mitad derecha
        else:
            derecha = medio - 1 # Si el objetivo es menor, busca en la mitad izquierda
    return -1 # Si no se encuentra el objetivo, devuelve -1

# --- Programa principal ---

# Se ordena la lista de patentes (usando la función de ordenamiento incorporada de Python)
lista_patentes_ordenada = sorted(lista_patentes)

print("---Busqueda BINARIA de patentes en lista.---")
print("Ejemplo: NYG296 o PNZ619")
patente = input("Ingrese la patente interesada en buscar: ") # Pide al usuario la patente a buscar

inicio_lineal = time.time() # Comienza a medir el tiempo de la búsqueda
resultado = busqueda_binaria(lista_patentes_ordenada, patente) # Ejecuta la búsqueda binaria
if resultado != -1:
    print(f"El automovil patente {resultado} se encuentra en la base de datos.") # Muestra el resultado si se encuentra
else:
    print("Patente no encontrada.") # Informa si no se encontró

fin_lineal = time.time() # Termina de medir el tiempo
# Muestra el tiempo total que tomó la búsqueda
print(f"---Tiempo de busqueda: {(fin_lineal - inicio_lineal):.6f} seg---")