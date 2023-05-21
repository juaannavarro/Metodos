import numpy as np

F1 = [1, 0 , 0 ,0 ,0 ,0, 0 ,0, 0 ,0 ,0 ,0]
F2 = [1, 6, 36, 216, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0]
F3 = [0,0,0,0,1,0,0,0,0,0,0,0]
F4 = [0,0,0,0,1,6,36,216,0,0,0,0]
F5 = [0,0,0,0,0,0,0,0,1,0,0,0]
F6 = [0,0,0,0,0,0,0,0,1,6,36,216]
F7 = [0,1,12,108,0,-1,0,0,0,0,0,0]
F8 = [0,0,2,36,0,0,-2,0,0,0,0,0]
F9 = [0,0,0,0,0,1,12,108,0,-1,0,0]
F10 = [0,0,0,0,0,0,2,36,0,0,-2,0]
F11 = [0,0,2,0,0,0,0,0,0,0,0,0]
F12 = [0,0,0,0,0,0,0,0,0,0,2,36]
b = [13,12,12,20,20,20,0,0,0,0,0,0]

A = np.array([F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12])
x = np.linalg.solve(A, b) #Solucion
coeficientes = ['a0', 'a1', 'a2', 'a3', 'b0', 'b1', 'b2', 'b3', 'c0', 'c1', 'c2', 'c3']
solucion = {}

for i in range(12):
    solucion[coeficientes[i]] = round(x[i], 4) #agreamos las soluciones a un diccionario, por cuestiones de orden

for i in solucion:
    print('{} = {}'.format(i, solucion.get(i))) #mostramos la solucion de cada coeficiente