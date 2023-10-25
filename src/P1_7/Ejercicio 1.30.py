#Inicio
#   Escribe "Introduce el numero de inicio"
#   Lee inicio
#   Escribe "Introduce el numero de incremento"
#   Lee incremento
#   Mientras (incremento <= 0) hacer
#       Lee incremento
#   Escribe "Introduce el numero total"
#   Lee total
#   Mientras (total <= 0) hacer
#       Lee total
#   contador = 0
#   Escribe inicio "-" end=""
#   Mientras (contador != (total-1)) hacer
#       contador += 1
#       inicio += incremento
#       Si (contador == total) entonces
#           Escribe "-" inicio
#       Sino
#           Si (contador == 1) entonces
#               Escribe inicio end=""
#       Sino
#           Escribe ".." inicio end=""
#Fin

inicio = int(input("Introduce el numero de inicio: "))
incremento = int(input("Introduce el numero de incremento: "))
while incremento <= 0:
    incremento = int(input("El numero de incremento debe ser mayor que 0: "))
total = int(input("Introduce el total de repeticiones: "))
while total <= 0:
    total = int(input("El numero de repeticiones debe ser mayor que 0: "))
contador = 0
print(str(inicio) + "-", end="")
while contador != (total - 1):
    contador += 1
    inicio += incremento
    if contador == (total -1):
        print("-" + str(inicio))
    elif contador == 1:
        print(str(inicio), end="")
    else:
        print(".." + str(inicio), end="")
