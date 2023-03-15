#importamos las bibliotecas necesarias
from statistics import linear_regression
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()


# Para este ejemplo crearemos 100 datos aleatorios del estilo (x,y)

rng = np.random.RandomState(1)
numero_datos= 100
x= 10 * rng.rand(numero_datos)
y= 3 *x -10 + rng.randn(numero_datos)## y= mx+b + ruido,  y=3x-10

plt.scatter(x,y)
##plt.show()

#Dividiremos los datos en un conjunto de entrenamiento y un conjunto de prueba

x_train= x[:80].reshape(-1,1)
y_train= y[:80].reshape(-1,1)

x_test = x[80:].reshape(-1,1)
y_test = y[80:].reshape(-1,1)

plt.scatter(x_train,y_train, color='red')
plt.scatter(x_test,y_test, color='blue')
##plt.show()

from sklearn.linear_model import LinearRegression
modelo_con_intercepto = LinearRegression(fit_intercept=True)##Clase de regresion lineal

modelo_con_intercepto.fit(x_train,y_train)##Entrenamos el modelo

x_fit = np.linspace(0,10,1000).reshape(-1,1)
y_fit = modelo_con_intercepto.predict(x_fit)

#plt.scatter(x_train,y_train, color='red')
#plt.plot(x_fit,y_fit, color='blue')
##plt.show()

##Podemos usar el modelo para predecir algun valor.

x_to_predict= [[5]]##valor independiente a predecir
y_to_predict= modelo_con_intercepto.predict(x_to_predict)##su valor dependiente de prediccion con el metodo predict.

print("El valor de y para x=",x_to_predict,"es: ",y_to_predict)

##x_to_predict= [[5.5],[7.3]]
#y_to_predict= modelo_con_intercepto.predict(x_to_predict)
#print("El valor de y para x=",x_to_predict,"es: ",y_to_predict)

###EJEMPLO 2

modelo_sin_intercepto = LinearRegression(fit_intercept=False)
modelo_sin_intercepto.fit(x_train,y_train)

x_fit = np.linspace(0,10,1000).reshape(-1,1)
y_fit = modelo_sin_intercepto.predict(x_fit)

#plt.scatter(x_train,y_train, color='red')
#plt.plot(x_fit,y_fit, color='green')
#plt.show()

##Mosrtar los parametros que definen el modelo.
print("Modelo con intercepto ajustado")
print("Coeficiente: ",modelo_con_intercepto.coef_)
print("Intercepto: ",modelo_con_intercepto.intercept_)
print("Modelo sin intercepto ajustado")
print("Coeficiente: ",modelo_sin_intercepto.coef_)
print("Intercepto: ",modelo_sin_intercepto.intercept_)

##Medmimos la calidad de los dos modelos

from sklearn.metrics import mean_squared_error ##vamos a calcular el error cuadratico medio de ambos modelos

y_for_mse_with_intercept = modelo_con_intercepto.predict(x_test)
y_for_mse_without_intercept = modelo_sin_intercepto.predict(x_test)

##calculamos el mse para ambos

mse_with_intercept = mean_squared_error(y_test,y_for_mse_with_intercept)
mse_without_intercept= mean_squared_error(y_test,y_for_mse_without_intercept)


##Calculamos el RMSE para ambos modelos

rmse_with_intercept = np.sqrt(mse_with_intercept)
rmse_without_intercept = np.sqrt(mse_without_intercept)

##Calculamos el R2 para ambos modelos

r2_with_intercept= modelo_con_intercepto.score(x_test,y_test)
r2_without_intercept= modelo_sin_intercepto.score(x_test,y_test)

print("MSE con intercepto: ",mse_with_intercept)
print("MSE sin intercepto: ",mse_without_intercept)
print("RMSE con intercepto: ",rmse_with_intercept)
print("RMSE sin intercepto: ",rmse_without_intercept)
print("R2 con intercepto: ",r2_with_intercept)
print("R2 sin intercepto: ",r2_without_intercept)






































