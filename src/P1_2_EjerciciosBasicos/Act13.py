# Ejercicio 2.13
# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los siguientes:
# "la división de n entre m da un cociente c y un resto r", donde n y m son los números introducidos por el usuario,
# y c y r son el cociente y el resto de la división entera respectivamente.
n = int(input("Introduce un numero: "))
m = int(input("Introduce otro numero: "))
c = n // m
r = n % m
print("la division de", n, "entre", m, "da un cociente", c, "y un resto", r)
