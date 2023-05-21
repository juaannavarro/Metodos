# <h1 align='center'>Metodos numéricos en el pronóstico del tiempo</h1>

---

<p align='center'>Ruben Nogueras, Paula Naranjo, Ignacio Pedrero y Juan Navarro</p>

---

[Pincha aqui para acceder al link del repositorio](https://github.com/juaannavarro/Metodos.git)

---

Los métodos numéricos desempeñan un papel fundamental en el pronóstico del tiempo al permitir el procesamiento y análisis de grandes cantidades de datos atmosféricos en un tiempo razonable. Estos métodos se utilizan para resolver las ecuaciones matemáticas complejas que describen el comportamiento de la atmósfera y así predecir su evolución futura.

El pronóstico del tiempo se basa en modelos numéricos de predicción, que dividen la atmósfera en una cuadrícula tridimensional y utilizan ecuaciones físicas para calcular cómo cambian las condiciones atmosféricas en cada punto de la cuadrícula con el tiempo. Sin embargo, debido a la complejidad de estas ecuaciones y la cantidad de datos involucrados, es necesario recurrir a métodos numéricos para obtener soluciones aproximadas.

---

Por otra parte, hemos desarrollado un codigo de python para la resolucion de un sistema de ecuaciones lineales de 12 ecuaciones, al hacer los splines cúbicos.
El codigo es el siguiente: 

```python3
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
coeficientes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
solucion = {}

for i in range(12):
    solucion[coeficientes[i]] = round(x[i], 4) #agreamos las soluciones a un diccionario, por cuestiones de orden

for i in solucion:
    print('{} = {}'.format(i, solucion.get(i))) #mostramos la solucion de cada coeficiente
```

La salida del codigo es la siguiente:

<img width="99" alt="image" src="https://github.com/juaannavarro/Metodos/assets/91721762/310d74d8-f0d7-4c9d-a1e7-eddaf93c2daa">


---
