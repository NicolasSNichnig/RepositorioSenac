notas = [10, 5.5, 8]

media1 = float(sum(notas)/len(notas))
print("-------------------------------")

print(notas)
print(f"A média atual é de: {media1}")

print("-------------------------------")

print(f"A menor nota é: {min(notas)}")
novaNota = input("Qual nota deseja mudar? ")

notas[notas.index(min(notas))] = int(novaNota)

print("-------------------------------")


notas.sort
print(notas)
print(f"A nova média é de: {float(sum(notas)/len(notas))}")