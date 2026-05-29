
import csv

archivo = open("datos/annual2010-2026.csv")

lector = csv.reader(archivo)

encabezado = next(lector)

temperatura_maxima = -999
temperatura_minima = 999

anio_maximo = ""
anio_minimo = ""

suma_temperaturas = 0
cantidad = 0

for fila in lector:

    temperatura = float(fila[2])

    suma_temperaturas = suma_temperaturas + temperatura
    cantidad = cantidad + 1

    if temperatura > temperatura_maxima:
        temperatura_maxima = temperatura
        anio_maximo = fila[1]

    if temperatura < temperatura_minima:
        temperatura_minima = temperatura
        anio_minimo = fila[1]

promedio = suma_temperaturas / cantidad

print("Temperatura mas alta:")
print(temperatura_maxima)

print("Año de temperatura maxima:")
print(anio_maximo)

print("Temperatura mas baja:")
print(temperatura_minima)

print("Año de temperatura minima:")
print(anio_minimo)

print("Promedio general de temperaturas:")
print(promedio)
