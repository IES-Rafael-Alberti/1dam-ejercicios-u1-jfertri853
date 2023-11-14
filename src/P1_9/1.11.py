def transformacion_rara(num):
    num = int((num * (num + 1)) / 2)
    return str(num)


numero = int(input("Introduce un numero: "))
print(transformacion_rara(numero))
