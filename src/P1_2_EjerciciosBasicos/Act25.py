# Ejercicio 2.25
# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla,
# el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan
# con un solo carácter.
fechaNacimiento = input("Introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")
fechaNacimiento = fechaNacimiento.split("/")
print("Day:", fechaNacimiento[0], "Month:", fechaNacimiento[1], "Year:", fechaNacimiento[2])
