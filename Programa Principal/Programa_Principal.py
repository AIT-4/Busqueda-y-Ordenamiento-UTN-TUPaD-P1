import csv # Módulo para trabajar con archivos CSV (separados por comas)
import time # Módulo para medir el tiempo de ejecución del código
import os # Módulo para interactuar con el sistema operativo (rutas de archivos)

lista_patentes = [] # Lista principal donde se almacenarán los datos de los vehículos

# Construye la ruta completa al archivo CSV de forma independiente del sistema operativo
script_dir = os.path.dirname(os.path.abspath(__file__)) # Obtiene el directorio actual del script
csv_path = os.path.join(script_dir, 'patentes.csv') # Une el directorio con el nombre del archivo CSV

# Abre y lee el archivo CSV
with open(csv_path, 'r', newline='') as archivo:
    lector = csv.DictReader(archivo) # Crea un lector que trata cada fila como un diccionario
    for fila in lector:
        lista_patentes.append(fila) # Añade cada fila (vehículo) a la lista_patentes

# El archivo patentes.csv tiene 100.000 elementos (patentes) con sus datos correspondientes del automovil.

# Define la función quicksort para ordenar la lista de vehículos por 'patente'
def quicksort(lista):
    # Caso base: si la lista tiene 0 o 1 elemento, ya está ordenada
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0] # Elige el primer elemento como pivot
        # Divide la lista en elementos menores o iguales al pivot y mayores al pivot
        less = [x for x in lista[1:] if x['patente'] <= pivot['patente']]
        greater = [x for x in lista[1:] if x['patente'] > pivot['patente']]
        # Combina las sublistas ordenadas con el pivot en el medio (recursividad)
        return quicksort(less) + [pivot] + quicksort(greater)

# Define la función busqueda_binaria para encontrar un vehículo por 'patente' en una lista ordenada
def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1 # Define los límites iniciales de la búsqueda
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2 # Calcula el índice del elemento medio
        patente_actual = lista[medio]['patente'] # Obtiene la patente del elemento medio
        if patente_actual == objetivo:
            return lista[medio] # Si encuentra la patente, devuelve el vehículo completo
        elif patente_actual < objetivo:
            izquierda = medio + 1 # Si la patente objetivo es mayor, busca en la mitad derecha
        else:
            derecha = medio - 1 # Si la patente objetivo es menor, busca en la mitad izquierda
    return -1 # Si la patente no se encuentra, devuelve -1

# Define una función para mostrar los detalles de un vehículo
def mostrar_vehiculo(vehiculo):
    print(f"El automóvil patente {vehiculo['patente']}, marca {vehiculo['marca']}, "
          f"modelo {vehiculo['modelo']}, año {vehiculo['anio']}, color {vehiculo.get('color', 'desconocido')} "
          f"se encuentra en la base de datos.")

# --- Inicio del programa principal ---
print("--- Ordenamiento con Quicksort de patentes en lista ---")
print("Primeros 3 vehículos sin ordenar:")
for v in lista_patentes[:3]: # Muestra los primeros 3 vehículos antes de ordenar
    mostrar_vehiculo(v)

# Sección de ordenamiento
inicio_tiempo_quicksort = time.time() # Registra el tiempo antes de iniciar el ordenamiento
lista_patentes_ordenada = quicksort(lista_patentes) # Llama a la función quicksort para ordenar la lista
fin_tiempo_quicksort = time.time() # Registra el tiempo después de que el ordenamiento finaliza

print("Primeros 3 vehículos ordenados por patente:")
for v in lista_patentes_ordenada[:3]: # Muestra los primeros 3 vehículos ya ordenados
    mostrar_vehiculo(v)

# Muestra el tiempo total que tomó el ordenamiento
print(f"---Tiempo de ordenamiento: {(fin_tiempo_quicksort - inicio_tiempo_quicksort):.6f} seg---")

print("\n" + "/" * 40 + "\n") # Separador visual

print("---Busqueda BINARIA de patentes en lista.---")
print("Ejemplo: NYG296 o PNZ619")
patente = input("Ingrese la patente interesada en buscar: ") # Pide al usuario la patente a buscar

# Sección de búsqueda
inicio_lineal = time.time() # Registra el tiempo antes de iniciar la búsqueda
resultado = busqueda_binaria(lista_patentes_ordenada, patente) # Llama a la función de búsqueda binaria
if resultado != -1:
    mostrar_vehiculo(resultado) # Si encuentra el vehículo, muestra sus datos
else:
    print("Patente no encontrada.") # Si no lo encuentra, informa al usuario

fin_lineal = time.time() # Registra el tiempo después de que la búsqueda finaliza
# Muestra el tiempo total que tomó la búsqueda
print(f"---Tiempo de busqueda: {(fin_lineal - inicio_lineal):.6f} seg---")