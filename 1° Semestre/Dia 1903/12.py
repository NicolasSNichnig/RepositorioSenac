tuple = ("maçã", "banana", "laranja")
print(tuple)

fruta = input("Insira sua fruta: ")

if(fruta in tuple):
    print("Está na tuple")
else:
    print("Não está na tuple")