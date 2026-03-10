# Leia estoque (int) e vendidas (int). Atualize com -= e mostre o estoque final.

estoque = int(input("Estoque atual"))
vendidas = int(input("Vendas"))

estoque -= vendidas
print(estoque)