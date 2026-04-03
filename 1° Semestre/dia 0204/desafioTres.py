number = int(input("Insira o número: "))

def par(numero):
    if(numero % 2 == 0):
        return "Par"
    else:
        return "Impar"
    
print(f"O número {number} é: {par(number)}")