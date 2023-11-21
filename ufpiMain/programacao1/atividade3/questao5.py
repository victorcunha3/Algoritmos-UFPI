from questao4 import alunosArmazenados

def alunosBusca(alunos, curso):
    alunos_encontrados = []
    for matricula, aluno in alunos.items():
        if aluno.get("curso") == curso:
            alunos_encontrados.append(aluno)
    return alunos_encontrados

cursoSolicitar= input("digite o curso que deseja procurar: ")
alunosALL = alunosBusca(alunosArmazenados, cursoSolicitar)

for aluno_atual in alunosALL:
    print(f"nome: {aluno_atual['nome']}")
    print(f"matricula: {aluno_atual['matricula']}")
    print(f"curso: {aluno_atual['curso']}")

#print(alunosALL)