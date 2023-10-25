# Ejercicio 2.16
# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un
# programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el
# precio habitual de una barra de pan (establecido en el programa como una constante), el descuento que se le hace por
# no ser fresca y el coste final total de todas las barras no frescas.
precioPan = 3.49
descuento = 0.6
panMaloVendido = int(input("Cuantas barras de pan que no son del dia se han vendido hoy: "))
print("El precio de la barra de pan es", precioPan)
print("El descuento del pan de ayer es del", descuento * 100, "%")
print("El precio total de la venta de panes de ayer es de: {:.2f}".format((panMaloVendido * (precioPan * (1 - 0.6)))))
