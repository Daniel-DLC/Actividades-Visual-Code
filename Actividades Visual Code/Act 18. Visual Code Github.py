#Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine. 
#Programa que solicita al usuario que introduzca el número de menores y adultos que asistirán al cine, y luego calcula y muestra el total a pagar aplicando los descuentos correspondientes.
menores = int(input("Introduce el número de menores: "))
adultos = int(input("Introduce el número de adultos: "))
total_menores = (menores * 12 * 0.5) 
total_adultos = (adultos * 12 * 0.9)
print("El precio total del cine para", menores, "menor/es es:", round(total_menores, 2), "euros")
print("El precio total del cine para", adultos, "adulto/s es:", round(total_adultos, 2), "euros")