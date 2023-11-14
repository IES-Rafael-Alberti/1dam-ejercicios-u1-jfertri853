def calcular_precio_con_iva(articulo, iva):
    print("El precio es de", articulo * ((iva / 100) + 1), "euros")


precioArticulo = float(input("Introduce el precio del articulo: "))
porcentajeIva = float(input("Introduce el IVA a aplicar: "))
calcular_precio_con_iva(precioArticulo, porcentajeIva)
