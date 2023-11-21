import pprint

dadosArmazenados = r"C:\Users\victo\OneDrive\Documentos\workTabMemory\UFPI\dados.txt"
alunosArmazenados = {}
aluno_atual = {}

with open(dadosArmazenados, "r") as lerArquivo:
    for linha_atual in lerArquivo:
        linha_atual = linha_atual.strip()
        chave, valor = linha_atual.split(": ", 1)
        aluno_atual[chave] = valor

        if "curso" in aluno_atual:
            alunosArmazenados[aluno_atual["matricula"]] = aluno_atual
            aluno_atual = {}

if __name__ == "__main__":
    pprint.pprint(alunosArmazenados)
