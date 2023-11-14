IVA = 0.1
importeFinal = float(input("Introduce la cantidad final que se ha pagado: "))
precioSinIva = importeFinal / (1 + IVA)
gastosDeIva = importeFinal - precioSinIva
print("El artículo sin IVA cuesta: {:.2f} has pagado {:.2f} de IVA".format(precioSinIva, gastosDeIva))
