# Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.

letra = input("Introduce una letra, número o símbolo: ")

if letra.islower():
    print("La letra es minúscula")
elif letra.isupper():
    print("La letra es mayúscula")
elif letra.isdigit():
    print("El valor introducido es un número")
else:
    print("El valor introducido es un símbolo")