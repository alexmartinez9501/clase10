import matplotlib.pyplot as plt


edades = [12, 15, 13, 12, 18, 20, 19, 20, 13, 12, 13, 17, 15, 16, 13, 14, 13, 17, 19]

intervalos = range(min(edades), max(edades) + 2) #calculamos los extremos de los intervalos

plt.hist(x=edades, bins=intervalos, color='#8892c6', rwidth=0.85)
plt.title('Histograma de edades')
plt.xlabel('Edades')
plt.ylabel('Frecuencia')
plt.xticks(intervalos)

plt.show() #dibujamos el histograma

#segundo gráfico
edades = [12, 15, 13, 12, 18, 20, 19, 20, 13, 12, 13, 17, 15, 16, 13, 14, 13, 17, 19]

intervalos = [10, 13, 16, 19, 22] #indicamos los extremos de los intervalos

plt.hist(x=edades, bins=intervalos, color='#3b83bd', rwidth=0.85,)
plt.title('Histograma de edades')
plt.xlabel('Edades')
plt.ylabel('Frecuencia')
plt.xticks(intervalos)

plt.show() #dibujamos el histograma

#tercer gráfico
tiempos = [12, 14, 15, 60, 55, 40, 30, 23, 42, 32, 21, 26, 25, 28, 10, 7, 36, 45, 55, 32, 17, 24, 21, 60, 49, 48, 3, 14, 19]

intervalos = [0, 10, 20, 30, 40, 50, 60]

plt.hist(x=tiempos, bins=intervalos, color='#9db896', rwidth=0.85,)
plt.title('Histograma de tiempos de llamadas')
plt.xlabel('Tiempos')
plt.ylabel('Frecuencia')
plt.xticks(intervalos)

plt.show()
