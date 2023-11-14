# Ejercicio 2.14
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa
# de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán
# en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de
# payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
def pesar_paquete(clown_amount, doll_amount):
    clown = 112.0
    doll = 75.0
    weight = (clown_amount * clown) + (doll_amount * doll)
    return weight


print("Haz tu pedido aqui")
cantidadPayasos = int(input("Introduce la cantidad de payasos: "))
cantidadMunnecas = int(input("Introduce la cantidad de munnecas: "))
print("El paquete pesa", pesar_paquete(cantidadPayasos, cantidadMunnecas), "gramos")
