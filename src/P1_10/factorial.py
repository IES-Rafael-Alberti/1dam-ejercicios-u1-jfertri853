def factorial(num: int):
    if num == 0:
        return 1

    for i in range(num - 1, 0, -1):
        num *= i
    return num


def factorial_str(num: int):
    if num == 0:
        return "0! => 1"

    cadena = str(num) + "!" + " => "
    resultado = 1
    for i in range(num, 0, -1):
        cadena += str(i)
        if i != 1:
            cadena += " x "
        else:
            cadena += " = "
        resultado *= i
    return cadena + str(resultado)


def main():
    numero = int(input("Introduce un numero: "))
    print(factorial(numero))
    print(factorial_str(numero))


if __name__ == "__main__":
    main()
