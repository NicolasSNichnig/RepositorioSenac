# Leia metros (int). Converta para km inteiros com //= 1000 e guarde metros restantes com %= (em outra variável).

metros = int(input("Insira os metros: "))

metrosRestantes = metros % 1000
metros //= 1000

print(metros, "km", "e", metrosRestantes, "metros")