precioNeto = float(input("Introduce el precio sin IVA del artículo: "))
iva = float(input("Introduce el porcentaje de IVA a aplicar: "))
iva = iva/100
print("El articulo cuesta: {:.2f} lereles".format(precioNeto * (iva + 1)))
