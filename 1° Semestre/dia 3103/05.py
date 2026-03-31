numberOne = int(input("Insira o número: "))
numberTwo = int(input("Insira o número: "))

if numberOne > numberTwo:
    print(f"{numberOne} é maior que {numberTwo}")
elif numberTwo > numberOne:
    print(f"{numberTwo} é maior que {numberOne}")
else:
    print("Os números são iguais.")