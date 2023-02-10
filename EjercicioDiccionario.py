import pandas as pd


frutas = {"Manzana": 3, "Pera": 2, "Naranja": 0, "Sandia": 5}


f = input("Ingrese el nombre de la fruta:")
if frutas.get(f) == None:
    print("La fruta no existe")
else:
 kilos = int(input("Ingrese la cantidad de kilos:"))
 print("El precio de la fruta es: ", frutas[f]*kilos)


