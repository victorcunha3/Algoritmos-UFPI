armazenar_alunos = []
arquivo = "dados.txt"
continuar_loop = True

while continuar_loop:
    nome = input("digite nome do aluno: ")
    matricula = input("digite a matrícula do aluno: ")
    curso = input("digite o curso do aluno: ")
    aluno = {
        "nome": nome,
        "matricula": matricula,
        "curso": curso,
    }
    armazenar_alunos.append(aluno)
    continuar_logado = input("deseja continuar no sistema? (S/N): ")

    if continuar_logado.upper() == "N":
        print(armazenar_alunos)
        continuar_loop = False

with open(arquivo, "w") as f:
    for aluno in armazenar_alunos:
        f.write(f"nome: {aluno['nome']}\n")
        f.write(f"matricula: {aluno['matricula']}\n")
        f.write(f"curso: {aluno['curso']}\n")
print("dados salvos")