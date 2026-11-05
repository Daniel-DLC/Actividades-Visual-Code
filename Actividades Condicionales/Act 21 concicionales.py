#Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo 
#Programa que introduciendo los 3 valores indica si la raiz es negativa y te da los resultados de la equación.
import math

a = float(input("Introduce a: "))
b = float(input("Introduce b: "))
c = float(input("Introduce c: "))

raiz = b**2 - 4*a*c

if raiz < 0:
    print("La raíz no puede ser un valor negativo")
else:
    x1 = (-b + math.sqrt(raiz)) / (2*a)
    x2 = (-b - math.sqrt(raiz)) / (2*a)

    print("El valor de x1 es: ", x1)
    print("El valor de x2 es: ", x2)