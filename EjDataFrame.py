import pandas as pd


tabla = pd.DataFrame({"Mes": ["Enero","Febrero","Marzo","Abril"],"Ventas": [1, 2, 3,4], "Gastos": [4, 5, 6, 7]})



print(tabla.head(2))##Dos primeras filas comenazando desde la primera
print("------------\n")
print(tabla.tail(1))##Ultima fila
print(tabla.info())##Informacion de la tabla
print(tabla["Mes"])##Imprime la columna MES de la tabla
print(tabla.iloc[:,2])  ##Imprime la columna 2 de la tabla  

tabla["Porcentaje"] = [10, 20, 30, 40] ##Agrega una columna a la tabla

print (tabla)

tabla.drop("Porcentaje", axis = 1, inplace = True) ##Elimina la columna porcentaje de la tabla
tabla