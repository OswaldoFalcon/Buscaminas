import sys
import numpy as np

with open(sys.argv[1], 'r') as f:  #leemos el archivo txt
    contents = f.read()
contenido = contents


size = [int(temp) for temp in contenido.split() if temp.isdigit()] # obtenemos el tamaño de la matriz

matriz = contenido.split("\n") # dividimos por salto de linea y sacamos elprimero 
matriz.pop(0)

ma=[]

for linea in range (len(matriz)):   
    ma.append(list(matriz[linea]))

ma = np.array(ma) # convertimos la matriz a numpy

a = np.zeros((size[0],size[1])) # creamos una del mismo tamaño pero con zeros 

for i in range(len(ma)):   # transformamos a numerica los asteristicos * = 1
    for j in range (len(ma[i])):
        if('*' != ma[i][j]):
            a[i][j] = 0
        elif (ma[i][j] == '*') :
            a[i][j] = -1

tablero = ma
max_i = size[0]

tablero = tablero.astype('object') #para trabajar con caracteres y ints
max_j= size[1]

for i in range(len(tablero)):  
    for j in range (len(tablero[i])):
        if('*' == tablero[i][j]):
            if (j+1) < max_j and  (a[i][j+1]) !=-1: #para que no se pasa del valor maximo de fila
                a[i][j+1] += 1 #derecha
            if (j-1) > 0 and  (a[i][j-1]) !=-1 :
                a[i][j-1] += 1 #izquierda
            if (i-1) > 0 and  (a[i-1][j]) !=-1 :
                a[i-1][j] += 1  #arriba
            if (i+1) < max_i and  (a[i+1][j]) !=-1 :
                a[i+1][j] += 1  #abajo
            if (i+1) < max_i and (j+1) < max_j and  (a[i+1][j+1]) !=-1 :
                a[i+1][j+1] += 1 #down derecha
            if (i+1) < max_i and (j-1) > 0 and  (a[i+1][j-1]) != -1 :
                a[i+1][j-1] += 1 #down izquierda
            if (i-1)>0 and (j-1) > 0 and  (a[i-1][j-1]) !=-1 :
                a[i-1][j-1] += 1 #up izquierda
            if (i-1) >0 and (j+1) < max_j and  (a[i-1][j+1]) !=-1 :
                a[i-1][j+1] += 1 #up derecha

a = a.astype('object') #usamos este tipo para tener Caracteres con numeros

for i in range(len(a)):        #modificamos -1 a *
    for j in range (len(a[i])):
        if(-1 == a[i][j]):
            a[i][j] = '*'

print(a)

