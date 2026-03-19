fila = ["Ana", "Bruno"]
print(fila)

cliente1 = input("Uma nova pessoa chegou: ")
cliente2 = input("Uma nova pessoa chegou: ")

novasPessoas = [cliente1, cliente2]

fila.extend(novasPessoas)
print(fila)

clientePrioritário = input("Cliente prioritário: ")

fila.insert(1, clientePrioritário)
print(fila)

print(" ")
print("Atendimento...")
print(" ")

fila.pop(0)
print(fila)