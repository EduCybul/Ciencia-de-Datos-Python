#importamos las bibliotecas necesarias 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import preprocessing # para el procesado de datos.

# importamos los datos 

url = 'https://raw.githubusercontent.com/jamaltoutouh/curso-ciencia-de-datos-python/main/insurance.csv'
insurance = pd.read_csv('insurance.csv')

#Mostramos la informacion de los datos
print('Atributos del conjuntos de datos: ', insurance.columns)
print('Dimensiones del conjunto de datos: ', insurance.shape)

print('Numero de filas: ', insurance.shape[0])
print ('Numero de columnas: ', insurance.shape[1])


print(insurance.head())

print(insurance.info())

##Agrupamos las colmnas por tipo de datos: continuas, contables y categoricas.

columnas_continuas = ['age', 'bmi', 'children', 'charges']
columnas_categoricas= ['sex', 'smoker', 'region']

#Tratamos ambas columnas y despues las concatenamos

#Tratamiento de las columnas categoricas

print('sex: ')
print(insurance['sex'].value_counts())
print('---------------------------------')
print('smoker: ')
print(insurance['smoker'].value_counts())
print('---------------------------------')
print('region: ')
print(insurance['region'].value_counts())

columnas_categoricas_01=['sex', 'smoker']
columnas_categoricas_mult=['region']

#Definimos los mapeos para las columnas categoricas 01
sex_map = {'male':0, 'female':1}
smoker_map = {'yes':1, 'no':0}

#Aplicamos los mapeos a las columnas categoricas 01.
insurance['sex'] = insurance['sex'].map(sex_map)
insurance['smoker'] = insurance['smoker'].map(smoker_map)

print(insurance.head())

#Tratamiento de las columnas categoricas multiclase

onehot = preprocessing.OneHotEncoder(dtype=int)
oh_encoded_columns= onehot.fit_transform(insurance[columnas_categoricas_mult])

datos_categoricos_multi = pd.DataFrame(oh_encoded_columns.toarray())

#Para mostrar como queda creamos un dataframe con los nombre de las categorias que teniamos
datos_categoricos_aux= datos_categoricos_multi.copy()
datos_categoricos_aux['region'] = insurance['region']
print(datos_categoricos_aux)

#concatenamso los datos categoricos
datos_categoricos = pd.concat([datos_categoricos_multi, insurance[columnas_categoricas_01]], axis=1)
datos_categoricos.head()

#Tratamiento de las columnas continuas

#Definimos el encoder

standarscaler = preprocessing.StandardScaler().fit(insurance[columnas_continuas])

#Aplicamos el encoder

ssd_encoded_columnas = standarscaler.transform(insurance[columnas_continuas])

#Creamos un dataframe con los datos continuos

datos_continuos = pd.DataFrame(ssd_encoded_columnas, columns=columnas_continuas)

#mostramos los datos continuos
print(datos_continuos.head())

#Concatenamos los datos continuos y categoricos

dataset = pd.concat([datos_categoricos, datos_continuos], axis=1)

#Mostramos el dataset
print(dataset.head())


#mostramos la informacion del dataset

print('Atributos del conjuntos de datos: ', dataset.columns)
print('Dimensiones del conjunto de datos: ', dataset.shape)


