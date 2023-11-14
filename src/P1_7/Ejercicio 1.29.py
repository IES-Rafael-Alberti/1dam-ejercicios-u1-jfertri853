#Inicio
#   Escribe "Introduce tu nombre: "
#   Lee nombre
#   Si (nombre == ""):
#       nombre = "Desconocido"
#   Escribe "Introduce tu edad: "
#   Lee edad
#   Mientras (edad < 0 or edad > 125) hacer
#       Escribe "Debes tener entre 0 y 125 años"
#       Lee edad
#   tiempoRestante = 125 - edad
#   Escribe "Te llamas " nombre " y tienes " edad " años, te quedan aún " tiempoRestante " años por cumplir"
#Fin

nombre = input("Introduce tu nombre: ")
if nombre == "":
    nombre = "Desconocido"
edad = int(input("Introduce tu edad: "))
while edad < 0 or edad > 125:
    edad = int(input("Debes tener entre 0 y 125 años, introduce tu edad: "))
tiempoRestante = 125 - edad
print("Te llamas", nombre, "y tienes", edad, "años, te quedan aun", tiempoRestante, "años por cumplir")
