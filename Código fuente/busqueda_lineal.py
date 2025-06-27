import csv # Módulo para trabajar con archivos CSV (Comma Separated Values)
import time # Módulo para medir el tiempo de ejecución del código
import os # Módulo para interactuar con el sistema operativo (útil para rutas de archivos)

lista_patentes = [] # Lista principal donde se almacenarán los datos completos de los vehículos (como diccionarios)

# Construye la ruta completa al archivo CSV de forma independiente del sistema operativo
script_dir = os.path.dirname(os.path.abspath(__file__)) # Obtiene el directorio donde se encuentra este script
csv_path = os.path.join(script_dir, 'patentes.csv') # Combina el directorio con el nombre del archivo CSV

# Abre y lee el archivo CSV
with open(csv_path, 'r') as archivo:
    lector = csv.DictReader(archivo) # Crea un lector que trata cada fila del CSV como un diccionario
    for fila in lector:
        lista_patentes.append(fila) # Añade cada fila completa (diccionario con todos los datos del vehículo) a la lista

# El archivo patentes.csv tiene 100.000 elementos (patentes) con sus datos correspondientes del automóvil.

## ALGORITMOS DE BUSQUEDA

# Función de Búsqueda Lineal
def busqueda_lineal(lista, objetivo):
    # Recorre la lista elemento por elemento desde el principio hasta el final
    for i in range(len(lista)):
        # Compara la 'patente' de cada vehículo con el 'objetivo' buscado
        if lista[i]['patente'] == objetivo:
            return lista[i] # Si encuentra la patente, devuelve el diccionario completo del vehículo
    return -1 # Si la patente no se encuentra después de revisar toda la lista, devuelve -1

# --- Programa principal ---

print("---Busqueda LINEAL de patentes en lista de diccionarios.---")
print("Ejemplo: NYG296 o PNZ619")
patente = input("Ingrese la patente interesada en buscar: ") # Pide al usuario la patente a buscar

inicio_lineal = time.time() # Comienza a medir el tiempo justo antes de iniciar la búsqueda
resultado = busqueda_lineal(lista_patentes, patente) # Llama a la función de búsqueda lineal
if resultado != -1:
    # Si encuentra el vehículo (resultado no es -1), muestra los detalles usando el diccionario retornado
    print(f"El automovil es un {resultado['marca']} modelo {resultado['modelo']} del año {resultado['anio']}")
else:
    print("Patente no encontrada.") # Informa al usuario si la patente no fue hallada

fin_lineal = time.time() # Termina de medir el tiempo justo después de que la búsqueda finaliza
# Muestra el tiempo total que tomó la búsqueda lineal, formateado a 6 decimales
print(f"---Tiempo de busqueda: {(fin_lineal - inicio_lineal):.6f} seg---")