# Ejercicio 2.27
# Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla
# una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de
# unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
nombreProducto = input("Introduce el nombre del producto: ")
precioProducto = float(input("Introduce el precio del producto: "))
numUnidades = int(input("Introduce la cantidad de productos: "))
costeTotal = precioProducto * numUnidades
print("{} {:09.2f} {:03d} {:011.2f}".format(nombreProducto, precioProducto, numUnidades, costeTotal))
