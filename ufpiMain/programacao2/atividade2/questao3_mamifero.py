"""Crie uma classe Mamifero que herde da classe Animal e obedeça à seguinte descrição:
 Possui um atributo alimento (str)
 Crie um método construtor que receba por parâmetro os valores iniciais de cada um dos 
atributos (incluindo
os atributos da classe Animal) e atribua-os aos seus respecƟvos atributos.
 Crie os métodos geƩer e seƩer (usando @property) para cada um dos atributos 
para o atributo alimento.
 Estenda o método dados sem parâmetros e sem retorno, que, quando chamado, 
imprime na tela uma espécie
de relatório informando os dados do mamífero (incluindo os dados do Animal e 
mais o alimento)."""
from questao1_animal import Animal

def relatorio_mamifero(metodo_dados):
    def modificar_acao(self):
        metodo_dados(self)
        print(f"alimentação: {self.alimento}")
        print(f"nome: {self.nome}")
        print(f"comprimento: {self.comprimento}")
        print(f"patas: {self.patas}")
        print(f"cor: {self.cor}")
        print(f"ambiente: {self.ambiente}")
        print(f"velocidade: {self.velocidade}")
    return modificar_acao

class Mamifero(Animal):
    def __init__(self, nome: str, comprimento: float, patas: int, cor: str, 
                 ambiente: str, velocidade: float, alimento: str) -> None:
        super().__init__(nome, comprimento, patas, cor, ambiente, velocidade)

        self._alimento = alimento

    @property
    def alimento(self):
        return self._alimento
    
    @alimento.setter
    def alimento(self, valor):
        self._alimento = valor

    @relatorio_mamifero
    def dados(self) -> str:
        ...
    

if __name__ == "__main__":
    mamifero1:Mamifero = Mamifero('dog',60,4,'marrom','terrestre',5,'ração')
    mamifero1.dados()
    
