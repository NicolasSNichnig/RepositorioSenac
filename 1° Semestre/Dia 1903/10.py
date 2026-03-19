agenda = {
    "Ana": "1111-1111", 
    "Bruno": "2222-2222"
}

print(f"A sua agenda é: {agenda}")

nome = input("Nome do novo contato: ")
number = input("Numero do novo contato: ")

if(nome in agenda):
    agenda.pop(nome)

agenda[nome] = number

remover = input("Insira um nome existente caso queira remover: ")

if(remover in agenda):
    agenda.pop(remover)

print(sorted(agenda.keys()))