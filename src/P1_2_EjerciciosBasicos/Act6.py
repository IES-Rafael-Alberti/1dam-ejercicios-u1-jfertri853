# Ejercicio 2.6
# Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha
# pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).
IVA = 0.1
importeFinal = float(input("Introduce la cantidad final que se ha pagado: "))
precioSinIva = importeFinal / (1 + IVA)
gastosDeIva = importeFinal - precioSinIva
print("El artículo sin IVA cuesta:", precioSinIva, ", has pagado", gastosDeIva, "de IVA")
