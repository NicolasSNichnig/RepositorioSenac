age = int(input("Qual sua idade: "))

if age <= 11:
    print("Criança")
elif age > 11 and age <= 17:
    print("Adolescente")
elif age > 17 and age <= 59:
    print("Adulto")
else:
    print("Idoso")