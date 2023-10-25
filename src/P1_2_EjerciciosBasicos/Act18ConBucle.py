nombre = input("Introduce tu nombre completo: ")
print(nombre.lower())
print(nombre.upper())
nombre = nombre.split(" ")
for i in range(0, len(nombre)):
    print(nombre[i].capitalize(), end=" ")
