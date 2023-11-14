#Inicio
#	Escribe "Introduce un numero entero: "
#	Lee numA
#   Escribe "Introduce otro numero entero: "
#   Mientras (numA == numB):
#	    Escribe "Error los numeros no pueden ser iguales"
#	    Lee numB
#   diferencia = (numA - numB)
#   si (diferencia < 0) entonces
#       diferencia *= -1
#   Si (numA<numB) entonces
#       Escribe numA " es menor que " numB " por una diferencia de " diferencia " numeros"
#   Sino:
#       Escribe numB " es menor que " numA " por una diferencia de " diferencia " numeros"
#Fin

numA = int(input("Introduce un numero: "))
numB = int(input("Introduce otro numero: "))
while numA == numB:
    numB = int(input("Error, los numeros no pueden ser iguales: "))
diferencia = numA - numB
if diferencia < 0:
    diferencia *= -1
if numA < numB:
    print(numA, "es menor que", numB, "por una diferencia de", diferencia, "numeros")
else:
    print(numB, "es menor que", numA, "por una diferencia de", diferencia, "numeros")
