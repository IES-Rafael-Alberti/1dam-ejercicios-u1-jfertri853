def conversion_a_celsius():
    grados_fahrenheit = float(input("Introduce los grados Fahrenheit: "))
    grados_celsius = (grados_fahrenheit - 32) * 5/9
    return grados_celsius


print(conversion_a_celsius())
