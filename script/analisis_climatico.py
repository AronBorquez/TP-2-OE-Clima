
import csv

archivo = open("datos/annual2010-2026.csv")

lector = csv.reader(archivo)

encabezado = next(lector)

for fila in lector:
    print("Año:", fila[1], "- Temperatura promedio:", fila[2])
