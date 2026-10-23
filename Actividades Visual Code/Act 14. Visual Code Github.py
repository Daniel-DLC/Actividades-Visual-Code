#Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería math y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal. diametro = float(input("Introduce el valor del diámetro del círculo: "))
#
import math
diametro = float(input("Introduce el valor del diámetro del círculo: "))
radio = diametro / 2
print ("El área del círculo es:", round(math.pi * radio**2, 1))
print ("El perímetro del círculo es:", round(2 * math.pi * radio, 1))
