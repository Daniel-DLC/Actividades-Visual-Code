# Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.
letra = input("Introduce una letra: ")

if letra.isalpha():
    mayuscula = False

    if letra == letra.upper():
        mayuscula = True

    if mayuscula == True:
        print("Está en mayúscula")
    else:
        print("No está en mayúscula")
else:
    print("Error: no has introducido una letra")
