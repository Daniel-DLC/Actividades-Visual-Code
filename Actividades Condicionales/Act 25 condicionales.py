#Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos. 
nota = float(input("Introduce tu nota entre 1 y 10: "))

while nota < 1 or nota > 10:
    nota = float(input("Error. Introduce una nota entre 1 y 10: "))

if nota < 5 and nota > 0 :
    print ("Has sacado un:", nota, "y has sacado un insuficiente")
elif nota < 7 and nota > 4:
    print ("Has sacado un:", nota, "y has sacado un satisfactorio")
elif nota < 9 and nota > 6:
    print ("Has sacado un:", nota, "y has sacado un notable")
else:
    print ("Has sacado un:", nota, "y has sacado un excelente")