listaNumbers = [1, 2, 3, 4, 5, 6]

print(listaNumbers)
numeroRemovido = int(input("Qual número deseja remover: "))

if(numeroRemovido in listaNumbers):
    listaNumbers.remove(numeroRemovido)
    print(f"O item removido foi {numeroRemovido} e o tamanho da lista agora é: {len(listaNumbers)}")
