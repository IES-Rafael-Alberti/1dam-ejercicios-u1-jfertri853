num = 3
total = int(input("Dime cuantos numeros debe tener la serie: "))

contador = 1
while contador <= total:
    print(num, end="")
    if contador < total:
        print(" ", end="")
    num += 3
    contador += 1