##Programa para crear una tabla de ventas de una empresa mediante un diccionario
##y aplicar un descuento del 10% a las ventas
import pandas  as pd

inicio = int(input("Ingrese el año de inicio: "))
fin = int(input("Ingrese el año de fin: "))

ventas = {}

for i in range(inicio, fin + 1):
    ventas[i] = float(input("Introduce las ventas del año: " + str(i) + ": "))

ventas = pd.Series(ventas)

print("Ventas\n", ventas)

print("Ventas con descuento\n", ventas*0.9)










