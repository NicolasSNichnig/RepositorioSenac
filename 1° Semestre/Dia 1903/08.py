produto = {
    "nome": str, 
    "preco": float
}

produto["nome"] = input("Qual o nome do produto? ")
produto["preco"] = float(input("Qual o preço do produto? "))

print(produto)

if("desconto" in produto):
    produto.pop("desconto", 0)
    print(produto)
else:
    print("não há desconto para o produto")
    print(produto)