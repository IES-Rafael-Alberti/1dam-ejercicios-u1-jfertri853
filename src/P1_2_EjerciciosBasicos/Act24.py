# Ejercicio 2.24
# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por
# pantalla el número de euros y el número de céntimos del precio introducido.
precioProducto = float(input("Introduce el precio del producto: "))
precioProducto = str(precioProducto)
print("El producto cuesta", precioProducto.split(".")[0], "euros y", precioProducto.split(".")[1], "centimos")
