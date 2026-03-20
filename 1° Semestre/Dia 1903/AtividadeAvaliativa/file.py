catalogoLista = [("Maçã", 2.80), ("Banana", 3.0), ("Salgadinho", 10.0)]
estoqueDict = {
    "Maçã": 2,
    "Banana": 3,
    "Salgadinho": 4,
}

carrinho = []

def crudMenu(escolha):
    print(f"Escolha sua ação: \n 1 - Adicionar\n 2 - Remover\n 3 - Atualizar\n 4 - Mostrar {escolha}\n 5 - Voltar")
    return int(input(" "))

def menu():
    print(f"Escolha o menu: \n 1 - Catalogo\n 2 - Estoque\n 3 - Carrinho \n 4 - Fechar app")
    escolha = int(input(" "))

    match escolha:
        case 1: 
            escolhaCrud = crudMenu("Catálogo")
            catalogoFunc(escolhaCrud)
        case 2:
            escolhaCrud = crudMenu("Estoque")
            estoqueFunc(escolhaCrud)
        case 3:
            escolhaCrud = crudMenu("Carrinho")
            carrinhoFunc(escolhaCrud)
        case 4:
            return
        case _:
            print("Opção incorreta")
            menu()
            
def estoqueFunc(escolha):
    match escolha:
        case 1:
            novoNome = input("Insira o novo produto: ")
            novaQuantidade = int(input("Insira a quantidade de itens: "))

            estoqueDict[novoNome] = novaQuantidade
        case 2:
            oldName = input("Insira o nome do item que deseja remover: ")

            estoqueDict.pop(oldName)
        case 3:
            oldName = input("Insira o nome do item que queira editar: ")

            for produto in estoqueDict:
                if produto == oldName:
                    newName = input("Insira o novo nome: ")
                    newQuantity = int(input("Insira a nova quantidade de itens: "))

                    estoqueDict.pop(produto)
                    estoqueDict[newName] = newQuantity
                    break
        case 4:
            print(estoqueDict)
    menu()

def catalogoFunc(escolha):
    match escolha:
        case 1:
            nome = input("Insira o nome do novo produto: ")
            preco = float(input("Insira o preço do novo produto: "))

            newProduct = (nome, preco)
            catalogoLista.append(newProduct)
        case 2:
            oldNome = input("Insira o nome do produto que deseja remover: ")

            for produto in catalogoLista:
                if produto[0] == oldNome:
                    catalogoLista.pop(produto.index(oldNome))
        case 3:
            oldNome = input("Insira o nome do produto que deseja atualizar: ")

            for produto in catalogoLista:
                if produto[0] == oldNome:
                    novoNome = input("Qual o novo nome do produto: ")
                    novoPreco = float(input("Qual o novo preço: "))

                    newProduct = (novoNome, novoPreco)
                    oldPos = produto.index(oldNome)
                    catalogoLista.pop(produto.index(oldNome))
                    catalogoLista.insert(oldPos, newProduct)
        case 4:
            print(catalogoLista)
    menu()

def carrinhoFunc(escolha):
    match escolha:
        case 1:
            itemCarrinho = input("Insira o item que quer por no carrinho: ")
            carrinho.append(itemCarrinho)
        case 2:
            oldName = input("Insira o item que queira remover: ")

            for produto in carrinho:
                if produto == oldName:
                    carrinho.remove(produto)
        case 3:
            oldName = input("Insira o item que queira atualizar: ")

            for produto in carrinho:
                if produto == oldName:
                    newName = input("Insira o novo nome")
                    oldPos = carrinho.index(produto)

                    carrinho.pop(oldPos)
                    carrinho.insert(oldPos, newName)
        case 4:
            print(carrinho)
    menu()

menu()