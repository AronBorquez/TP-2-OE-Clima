
import csv

archivo = open("datos/annual2010-2026.csv")

lector = csv.reader(archivo)

for fila in lector:
    print(fila)
