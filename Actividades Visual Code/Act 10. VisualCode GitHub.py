# Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar.
# Programa que mu
variable1 = float(input("Introduce el dividendo: "))
variable2 = float(input("Introduce el divisor: "))
if variable1 % 2 == 0:
    paridad = "par"
else:
    paridad = "impar"
print(f"El cociente es: ",variable1/variable2)
print(f"El resto es: ",variable1 % variable2)
print(f"El dividendo es {paridad}")
  

