def resaltar_palabra(cadena, caracter):
    frase_resaltada = ""
    for i in cadena:
        if i == caracter or i == caracter.lower():
            frase_resaltada = frase_resaltada + i.upper()
        else:
            frase_resaltada = frase_resaltada + i
    return frase_resaltada


frase = input("Introduce una frase: ")
palabra = input("Introduce una palabra: ")
print(resaltar_palabra(frase, palabra))
