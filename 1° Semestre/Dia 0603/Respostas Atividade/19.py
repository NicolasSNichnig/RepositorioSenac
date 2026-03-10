# Leia estoque (int). Subtraia venda com -=, depois reposição com +=, por fim %= 6.

estoque = int(input("Quantidade no estoque: "))

estoque -= 2
estoque += 3
estoque %= 6

print(estoque)