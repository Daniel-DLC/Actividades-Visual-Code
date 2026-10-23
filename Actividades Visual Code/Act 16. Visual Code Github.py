# Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un resultado entero. Haz que se muestre por pantalla los dos  resultados de todo el proceso (raíz y división). 
#
import math
numero1 = float(input("Introduce un número: "))
numero2 = float(input("Introduce otro número: "))
raiz_cuadrada = math.sqrt(numero1)
division = int(raiz_cuadrada / 2)
print("La raíz cuadrada de", numero1, "es: ", raiz_cuadrada)
print("El resultado de la división es:", division)
raiz_cuadrada = math.sqrt(numero2)
division = int(raiz_cuadrada / 2)
print("La raíz cuadrada de", numero2, "es: ", round(raiz_cuadrada, 1))
print("El resultado de la división es:", division)