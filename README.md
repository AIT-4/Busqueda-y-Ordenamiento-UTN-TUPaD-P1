# Trabajo Practico Integrador
### Tecnicatura Universitaria en Programación a Distancia
### Programación 1 - Comisión 13

Integrantes:
- Elichiribehety Fernando. Contacto: fernando.elichiribehety@tupad.utn.edu.ar
- Durussel Federico. Contacto: federico.durussel@tupad.utn.edu.ar


## Algoritmos de Búsqueda y Ordenamiento en Python
Para nuestro trabajo integrador elegimos como eje temático **búsqueda y ordenamiento**. Este tema nos permite profundizar en los algoritmos que se utilizan para las diferentes tareas de búsqueda en programas y aplicaciones web que utilizamos a diario.

Estos son importantes para el manejo eficiente de datos, ya que ayudan a optimizar, organizar y mejorar las búsquedas. Por ejemplo, las aplicaciones de comercio en internet utilizan el ordenamiento para clasificar sus productos por precio,disponibilidad,etc. Los motores de búsqueda los utilizan para ordenar los resultados por importancia o popularidad. Queda claro que estos deben ser algoritmos mas complejos pero como primera aproximación es importante ver donde se utilizas y que aplicación real se puede observar.

El ordenamiento como uno de los pilares nos permite recuperar los datos e información de manera mucho mas rápida y eficiente, siempre y cuando, sepamos combinarlo con el método correcto de búsqueda.

Para este trabajo hemos investigado los diferentes algoritmos de búsqueda y de ordenamiento para luego elegir los adecuados para una base de datos (en este caso un archivo de planilla de cálculos) en el que se guarda información, ficticia, de automóviles.

## Contenido del repositorio

El contenido del repositorio se divide en dos carpetas la de:
- [Código Fuente](https://github.com/AIT-4/Busqueda-y-Ordenamiento-UTN-TUPaD-P1/tree/main/C%C3%B3digo%20fuente) donde se encuentran los archivos .py de las pruebas de busqueda y ordenamiento que hicimos sobre la hoja de calculo.
- [Programa Principal](https://github.com/AIT-4/Busqueda-y-Ordenamiento-UTN-TUPaD-P1/tree/main/Programa%20Principal) donde se encuentré el programa principal que elaboramos seleccionado los algoritmos adecuados.

### Descarga del código

Para la descarga del código debe clonarse el repositorio desde la terminal del sistema operativo o desde la integrada en el editor de código.
```bash
git clone https://github.com/AIT-4/Busqueda-y-Ordenamiento-UTN-TUPaD-P1.git
```
También se puede descargar el [archivo ZIP.](https://github.com/AIT-4/Busqueda-y-Ordenamiento-UTN-TUPaD-P1/archive/refs/heads/main.zip)

### Pruebas

Se pueden realizar pruebas con solo descargar el código. Se utilizaron las funciones `script_dir = os.path.dirname(os.path.abspath(__file__))` y
`csv_path = os.path.join(script_dir, 'patentes.csv')` para garantizar que desde cualquier sistema operativo funcione.

Desde la consola ingresar a la carpeta donde se encuentran los archivos .py (ejemplo: `Busqueda-y-Ordenamiento-UTN-TUPaD-P1/Código fuente`) y ejecutar:
```bash
python3 busqueda_lineal.py
```
donde dice `busqueda_linea.py` cambiar el archivo a ejecutar.

> **Importante:** Si va a ejecutar `ordenamiento_de_burbuja.py`, `ordenamiento_de_insercion.py` y `ordenamiento_de_seleccion.py` tenga en cuenta que estos van a tardar demasiado y el procesamiento se elevara en su computadora. La cantidad de registros de la hoja de calculo para este tipo de ordenamiento es mucho por lo que se tomara bastante tiempo. Estos algoritmos son para listas mas pequeñas.
> En la ultima linea del código puede encontrar un comentario donde indica el tiempo que tardo la prueba.
> Si quiere ejecutarlos debe modificar la hoja de cálculos eliminado los registros hasta que le queden solo 20 como para asegurar una prueba mas acorde con el algoritmo.

## Reflexiones del Equipo

Este trabajo integrador sobre algoritmos de búsqueda y ordenamiento en Python ha sido una experiencia enriquecedora y desafiante para ambos integrantes del equipo. Nos permitió no solo aplicar los conocimientos teóricos adquiridos en la cátedra de Programación 1, sino también enfrentarnos a escenarios más cercanos a la realidad de la programación.
Este proyecto nos permitió consolidar nuestros conocimientos en la selección, implementación y análisis de algoritmos. Entendemos ahora que la elección del algoritmo correcto y la estructura de datos adecuada pueden tener un impacto significativo en el rendimiento de una aplicación, especialmente con grandes volúmenes de información.