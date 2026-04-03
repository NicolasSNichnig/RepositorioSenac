palindromo = input("Insira sua palavra: ")



def ehPalindromo(palavra):
    palavraInvertida = ""
    for char in palavra:
        palavraInvertida = char + palavraInvertida
    if(palavraInvertida == palavra):
        return("É um palindromo")
    else:
        return ("Não é um palindromo")
        
print(ehPalindromo(palindromo))