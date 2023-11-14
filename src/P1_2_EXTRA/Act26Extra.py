listaCompra = input("Introduce los productos de la lista de la compra separados por coma y espacios: ")
listaCompra = listaCompra.replace(" ", "")
listaCompra = listaCompra.replace(",", "\n")
print(listaCompra)
