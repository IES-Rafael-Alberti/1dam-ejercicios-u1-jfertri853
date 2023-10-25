total = int(input("¿Cuantas notas vas a introducir? "))

while total < 1 or total > 100:
    print("Error - el numero de notas debe ser un numero entre 1 y 100")
    total = int(input("¿Cuantas notas vas a introducir? "))

print("Dame las", total, "notas del curso")

media = 0
contador = 1
while contador <= total:
    nota = float(input())
    media = media + nota
    contador += 1

media = media / total
print("La media es", media)
