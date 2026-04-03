listaCompras = []
valorCompra = 0

while True:
    valorCompra = int(input("Insira o valor da compra: "))

    if(valorCompra == 0):
        print("-----------------------------------------------")
        break
    else:
        listaCompras.append(valorCompra)
print(f"O total das compras é: {sum(listaCompras)}\nForam realizadas: {len(listaCompras)} compras \nA média da lista de compras é: {round(sum(listaCompras)/len(listaCompras), 2)}")
