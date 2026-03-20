catalogoItems = [("salgadinho", 13.99), ("chocolate", 6.70), ("Arroz", 10.0)]

estoqueItems = {
    "salgadinho": 4,
    "chocolate": 2,
    "Arroz": 20
}

carrinhoItems = []


def menu():
    print(f"Qual opção você deseja selecionar? \n 1 - Catalogo de produtos \n 2 - Estoque \n 3 - Carrinhos\n 4 - Fechar código")
    selecao = int(input(" "))

    match(selecao):
        case 1: 
            escolha = crudMenu("Catalogo")
            catalogo(escolha)
        case 2:
            escolha = crudMenu("Estoque")
            estoque(escolha)
        case 3:
            escolha = crudMenu("Carrinho")
        case 4:
            return
        case _:
            print("Opção não existente")
            menu()

def crudMenu(tipo):
    print(f"Escolha as opções:\n 1 - Adicionar \n 2 - Remover \n 3 - Atualizar \n 4 - Mostrar {tipo}")
    return int(input(" "))

def catalogo(escolha):
    match escolha: 
        case 1:
            nome = input("Insira o nome do novo produto: ")
            preco = float(input("Insira o preço do novo produto: "))

            catalogoItems.append((nome, preco))
        case 2:
            nome = input("Insira o nome do produto que deseja remover: ")

            for produto in catalogoItems:
                if(produto[0] == nome):
                    catalogoItems.remove(produto)
        case 3: 
            nome = input("Insira o nome do produto que deseja atualizar: ")
            for produto in catalogoItems:
                if(produto[0] == nome):
                    nome = input("Insira o novo nome: ")
                    preco = input("Insira o novo preço: ")
                    catalogoItems.remove(produto)
                    catalogoItems.append((nome, preco))
                    break
        case 4:
            print(f"O seu catalogo é: \n {catalogoItems}")
    menu()

def estoque(escolha):
    match escolha: 
        case 1:
            nome = input("Insira o nome do novo produto: ")
            preco = float(input("Insira o preço do novo produto: "))

            estoqueItems[nome] = preco
        case 2:
            nome = input("Insira o nome do produto que deseja remover: ")

            if(nome in estoqueItems):
                estoqueItems.pop(nome)
        case 3: 
            oldNome = input("Insira o nome do produto que deseja atualizar: ")
            for produto in estoqueItems:
                if(produto.index(nome)):
                    nome = input("Insira o novo nome: ")
                    preco = input("Insira o novo preço: ")
                    estoqueItems.pop(oldNome)
                    estoqueItems[nome] = preco
                    break
        case 4:
            print(f"O seu catalogo é: \n {estoqueItems}")
    menu()

menu()