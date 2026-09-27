#programa que pida los segundos y muestre por pantalla y en la misma frase los minutos y las horas
#Programa que solicita al usuario que introduzca un valor en segundos y luego calcula y muestra el equivalente en minutos y horas en la misma frase.
segundos = int(input("Introduce los segundos: "))

minutos = segundos / 60
horas = segundos / 3600

print("Minutos:", minutos, "Horas:", horas)