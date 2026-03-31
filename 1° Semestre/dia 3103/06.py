numberOne = int(input("Insira o número: "))
numberTwo = int(input("Insira o número: "))

tipo = int(input(f"Qual o tipo de calculo?\n 1 - Soma\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão\n"))

match tipo:
    case 1:
        print(numberOne + numberTwo)
    case 2:
        print(numberOne - numberTwo)
    case 3:
        print(numberOne * numberTwo)
    case 4:
        print(numberOne/numberTwo)