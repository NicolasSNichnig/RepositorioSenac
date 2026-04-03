numeros = []

for i in range(10):
    numero = int(input("Insira o número: "))
    numeros.append(numero)

for num in numeros:
    if(num > 10):
        print(f"O número {num} é maior que dez")
    elif(num < 10):
        print(f"O número {num} é menor que dez")
    else:
        print(f"O número {num} é igual à dez")