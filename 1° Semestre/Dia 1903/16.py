notaUm = float(input("Insira sua nota... "))
notaDois = float(input("Insira sua nota... "))
notaTres = float(input("Insira sua nota... "))

tupla = (notaUm, notaDois, notaTres)
mediaNotas = round(sum(tupla)/len(tupla), 2)

print(f"todas suas notas são: {tupla}")
print(f"A média das notas é {mediaNotas}")