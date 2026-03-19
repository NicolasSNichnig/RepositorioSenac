produto = {
    "nome": str, 
    "preco": float, 
    "quantidade": int
}

produto["nome"] = input("Qual o nome do produto? ")
produto["preco"] = float(input("Qual o preço do produto? "))
produto["quantidade"] = int(input("Quantos produtos? "))

produto["preco"] = (produto["preco"] * 0.5) + produto["preco"]
produto["quantidade"] += 2

total = produto["preco"] * produto["quantidade"]
print(f"O valor total é de: {total}")