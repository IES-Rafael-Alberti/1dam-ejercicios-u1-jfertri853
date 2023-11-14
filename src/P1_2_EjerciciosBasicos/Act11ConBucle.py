def sumatorio(num):
    total = 0
    for i in range(1, num + 1):
        total = total + i
    return total


numero = int(input("Introduce un numero: "))
resultado = sumatorio(numero)
print("El total es:", resultado)
