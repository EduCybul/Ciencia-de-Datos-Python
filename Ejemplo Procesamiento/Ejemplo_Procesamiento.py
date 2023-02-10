##Preparacion de datos para ser empleados por un modelo como las Redes neuronales Artificiales.

#Importamos las librerias necesarias

##%matplotlib inline 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns; sns.set()

from sklearn import preprocessing # para el procesado de datos.

#importamos los datos, cargamos el conjunto de datos.
url_data= "https://raw.githubusercontent.com/jamaltoutouh/curso-ciencia-de-datos-python/main/real-state.csv"
##real_state = pd.read_excel('state.xlsx', sheet_name='Sheet 1') ##leer los datos como un archivo excel
real_state = pd.read_csv(url_data) ##leer los datos como un archivo csv en una url.

#Mostramos informacion de los datos
print("Atributos del conjunto de datos: ", real_state.columns)
print("Dimensiones del conjunto de datos: ", real_state.shape)


print(real_state.head()) #mostramos los primeros 5 datos del conjunto de datos. La funcion head() nos devuelve n= 5 datos por defecto.

real_state.drop('No', axis=1, inplace=True)# eliminamos la columna No, ya que no es necesaria para el modelo.
print(real_state.head())

real_state.info() #mostramos informacion de los datos.

##Intentamos agrupar las columnas por categorias : continuas, contables y categoricas.

#Vemos cuales son los valores unicos de columnas de valores enteros.
print(real_state['X4 number of convenience stores'].value_counts()) #mostramos la cantidad de datos por cada valor de la columna X4 number of convenience stores.

columnas_continuas = ['X1 transaction date', 'X2 house age', 'X3 distance to the nearest MRT station', 'X5 latitude', 'X6 longitude', 'Y house price of unit area']
columnas_categoricas = ['X4 number of convenience stores']

## Vamos a tratar las columnas continuas y categoricas por separado.
# para luego concatenarlas en un solo conjunto de datos.

##Tratamiento de las columnas categoricas.

#Definimos el encoder 
onehot = preprocessing.OneHotEncoder(dtype=int)

#Aplicamos el cambio 
oh_encoded_columns = onehot.fit_transform(real_state[columnas_categoricas])

#Creamos un dataframe para luego generar el conjunto de datos final.
datos_categoricos= pd.DataFrame(oh_encoded_columns.toarray(),columns=['0','1','2','3','4','5','6','7','8','9','10'])


#Para mostrar como ha quedado creamos un data frame auxiliar y lo concatenamos con las categorias que teniamos.
datos_categoricos_aux = datos_categoricos.copy()
datos_categoricos_aux['X4 number of convenience stores'] = real_state['X4 number of convenience stores']
print (datos_categoricos_aux.head())

#2 Tratamiento de las columnas continuas.
#definimos el encoder
standard_scaler= preprocessing.StandardScaler().fit(real_state[columnas_continuas])

#Aplicamos el cambio
ss_encoded_columns = standard_scaler.fit_transform(real_state[columnas_continuas])

#Creamos un dataframe para luego generar el conjunto de datos nuevo
datos_continuos = pd.DataFrame(ss_encoded_columns,columns=columnas_continuas)

print(datos_continuos.head())

# #----------------------------------------------
# # Si quisieramos usar MinMax scaler
# # Definimos el encoder
# minmaxscaler = preprocessing.MinMaxScaler(feature_range=(0, 1)).fit(realstate_dataset[columnas_continuas])
# # Aplicamos el cambio
# mm_encoded_columns = minmaxscaler.fit_transform(realstate_dataset[columnas_continuas])


# Concatenamos los nuevos datos generados
dataset = pd.concat([datos_categoricos, datos_continuos], axis=1)
print(dataset.head())

##Mostramos informacion de los datos.
print('Atributos del conjunto de datos: ', dataset.columns)
print('Dimensiones del conjunto de datos: ', dataset.shape)
print(dataset.info())