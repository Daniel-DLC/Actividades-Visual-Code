# Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para no distinguir entre mayúsculas y minúsculas
frase = "A quién madruga Dios ayuda."

frase = frase.lower()

print("madruga:", frase.find("MADRUGA".lower()))
print("Dios:", frase.find("DIOS".lower()))
print("ayuda:", frase.find("AYUDA".lower()))