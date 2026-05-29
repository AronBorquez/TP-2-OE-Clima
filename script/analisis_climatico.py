
import csv

archivo = open("datos/annual2010-2026.csv")

lector = csv.reader(archivo)

encabezado = next(lector)

temperatura_maxima = -999

anio_maximo = ""

for fila in lector:

    temperatura = float(fila[2])

    if temperatura > temperatura_maxima:
        temperatura_maxima = temperatura
        anio_maximo = fila[1]

print("La temperatura promedio mas alta fue:")
print(temperatura_maxima)

print("Ocurrio en el año:")
print(anio_maximo)
