# Ejercicio 2.5
# Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima
# por pantalla el precio final del artículo.
precioNeto = float(input("Introduce el precio sin IVA del artículo: "))
iva = float(input("Introduce el porcentaje de IVA a aplicar: "))
iva = iva/100
print("El articulo cuesta:", precioNeto * (1 + iva), "lereles")
