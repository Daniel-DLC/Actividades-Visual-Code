# Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.
# Programa que solicita al usuario que introduzca los valores del lado, base menor, base mayor y altura de un trapecio isósceles, y luego calcula y muestra el área y el perímetro del trapecio.
lado = float(input("Introduce el valor del lado: "))
base_menor = float(input("Introduce el valor de la base menor: ")) 
base_mayor = float(input("Introduce el valor de la base mayor: "))
altura = float(input("Introduce el valor de la altura: "))
print("El área del trapecio isósceles es:", ((base_mayor + base_menor) * altura) / 2)
print("El perímetro del trapecio isósceles es:", 2 * lado + base_mayor + base_menor)