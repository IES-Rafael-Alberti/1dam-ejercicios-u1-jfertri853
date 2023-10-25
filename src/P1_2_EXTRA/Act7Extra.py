def redondeo(num):
    parte_decimal = num - round(num)
    parte_decimal = round(parte_decimal * 100)
    rounded_num = round(num) + (parte_decimal / 100)
    return rounded_num


print("Introduce 3 numeros")
n1 = float(input("primer numero: "))
n2 = float(input("segundo numero: "))
n3 = float(input("tercer numero: "))
print("Sumatorio =", redondeo(n1 + n2 + n3))
