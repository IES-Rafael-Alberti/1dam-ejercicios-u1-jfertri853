numX = int(input("Introduce un numero: "))
numY = int(input("Introduce otro numero: "))
if numX <= numY:
    numInicial = numX
    numFinal = numY + 1
else:
    numInicial = numY
    numFinal = numX + 1

for i in range(numInicial, numFinal, 1):
    print(i, end="")
    if i != numFinal - 1:
        print("-", end="")
