# Ejercicio 2.4
# Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit
# e imprima por pantalla la temperatura convertida.
gradosCelsius = float(input("Introduce los grados Celsius: "))
gradosFahrenheit = (gradosCelsius * 1.8) + 32
print(gradosCelsius, "grados Celsius son", gradosFahrenheit, "grados Fahrenheit")
