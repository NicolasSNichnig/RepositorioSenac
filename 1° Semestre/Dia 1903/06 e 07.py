alunoName = input("Insira o nome do aluno: ")
alunoAge = int(input("insira a idade do aluno: "))

aluno = {
    "nome": alunoName,
    "idade": alunoAge,
    "nota": 0
}

print(aluno)
print(type(aluno))

### parte 2

nota = int(input("Qual a nota do aluno: "))
aluno["nota"] = nota

print(aluno)