def invertir_frase(frase_derecha):
    frase_invertida = ""
    for i in frase_derecha:
        frase_invertida = i + frase_invertida
    return frase_invertida


frase = str(input("Introduce una frase: "))
print(invertir_frase(frase))