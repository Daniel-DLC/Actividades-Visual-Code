#A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10 
#Programa que te obliga a introducir un numero entre 0 y 10 y te indica cual es mas grande o iguales.
num1 = int(input("Introduce un número del 0 al 10: "))

while num1 not in range(0, 11):
    num1 = int(input("Error. Introduce un número del 0 al 10: "))

num2 = int(input("Introduce otro número del 0 al 10: "))

while num2 not in range(0, 11):
    num2 = int(input("Error. Introduce un número del 0 al 10: "))

if num1 > num2:
    print("El primero es mayor")
elif num1 < num2:
    print("El segundo es mayor")
else:
    print("Son iguales")