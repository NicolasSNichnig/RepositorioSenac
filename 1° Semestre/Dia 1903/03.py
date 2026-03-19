num1 = int(input("Insira o numero: "))
num2 = int(input("Insira o numero: "))
num3 = int(input("Insira o numero: "))

listaNum = [num1, num2, num3]

listaNum[-1] = listaNum[0] + listaNum[1]
print(listaNum)