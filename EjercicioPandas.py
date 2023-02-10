import pandas as pd 

def estadisticas(notas):
    notas = pd.Series(notas)
    estadisticas = pd.Series([notas.min(), notas.max(), notas.mean(), notas.median(), notas.std()], index = ["Minimo", "Maximo", "Media", "Mediana", "Desviacion estandar"])

    return estadisticas

notas = {"Juan":9 , "Maria": 8, "Pedro": 7, "Luis": 6, "Ana": 5, "Jose": 4, "Rosa": 3, "Luisa": 2, "Marta": 1, "Pablo": 0}
print(estadisticas(notas))
