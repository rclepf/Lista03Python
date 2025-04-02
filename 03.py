quantidade_alunos = int(input("Informe a quantidade de alunos: "))

contador_alunos = 0

while contador_alunos < quantidade_alunos:
    nome = input(f"\nInforme o nome do {contador_alunos + 1}º aluno: ")
    
    nota1 = float(input("Informe a 1ª nota: "))
    nota2 = float(input("Informe a 2ª nota: "))
    nota3 = float(input("Informe a 3ª nota: "))

    media = (nota1 + nota2 + nota3) / 3

    print(f"\nAluno: {nome} | Média: {media:.2f}")

    contador_alunos += 1
