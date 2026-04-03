lista = []

while True:
    number = int(input("Coloque um número na lista: "))
    if(number == 0):
        break
    else:
        lista.append(number)

def mediaLista(listaNormal):
    return sum(listaNormal)/len(listaNormal)

print(f"A média da lista é de: {round(mediaLista(lista), 2)}")