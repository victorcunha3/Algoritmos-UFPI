"""Escreva uma classe cujos objetos representam alunos matriculados em uma disciplina.
Cada objeto dessa classe deve guardar os seguintes dados do aluno: matrícula, nome, 2
notas de prova e 1 nota de trabalho. Escreva os seguintes métodos para esta classe:
media => calcula a media final do aluno(cada prova tem peso 2,5 e trabalho peso2)
final => calcula quanto o aluno precisa para a prova final(retorna zero se ele nao estiver de prova final)"""
    
class AlunosMatriculados:
    def __init__(self, matricula: int, nome: str,
                  nota1:float, nota2:float, nota_trabalho: float) -> None:
        
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota_trabalho = nota_trabalho

    def media_aluno(self) -> float:
        media = ((self.nota1 * 2.5) + (self.nota2 * 2.5) + (self.nota_trabalho * 2)) / (2.5 + 2.5 + 2)
        media_float = f'{media:.1f}'
        return float(media_float)
    
    def final_aluno(self) -> float:
        media = self.media_aluno()
        if media < 7:
            final = (7 - media)
            final_transform = f'{final:.1f}'
            return float(final_transform)
        
        return 0

if __name__ == '__main__':
    aluno1 = AlunosMatriculados(12,'Victor',3,3.5,6)
    aluno2 = AlunosMatriculados(1243, 'Lorrana', 10, 7.8, 5)
    print("#### NOTA VICTOR ######")
    print(aluno1.media_aluno())
    print(aluno1.final_aluno())

    print("##### NOTA LORRANA #######")
    print(aluno2.media_aluno())
    print(aluno2.final_aluno())