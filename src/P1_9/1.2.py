def calcular_importe(horas, coste):
    return horas * coste


horasTrabajadas = int(input("Introduce las horas trabajadas: "))
precioHora = int(input("Introduce el precio de la hora: "))
importe = calcular_importe(horasTrabajadas, precioHora)
print("El importe es:", importe)
