"""2. Crie uma classe Peixe que herda da classe Animal e obedeça à seguinte descrição:
 Possui um atributo caracterisƟca (str)
 Crie um método construtor que receba por parâmetro os valores iniciais de cada um dos 
atributos (incluindo
os atributos da classe Animal) e atribua-os aos seus respecƟvos atributos.
 Crie os métodos geƩer e seƩer (usando @property) para o atributo caracterisƟca.
 Estenda o método dados sem parâmetros e sem retorno, que, quando chamado, imprime na 
tela uma espécie
de relatório informando os dados do peixe (incluindo os dados do Animal e mais a 
zcaracterísƟca). UƟlize um
@decorator para isso."""

from questao1_animal import Animal

def relatorio_peixe(metodo_dados):
    def modificar_acao(self):
        metodo_dados(self)
        print(f"quantidade de escamas: {self.quantidade_escama}")
        print(f"nome: {self.nome}")
        print(f"comprimento: {self.comprimento}")
        print(f"patas: {self.patas}")
        print(f"cor: {self.cor}")
        print(f"ambiente: {self.ambiente}")
        print(f"velocidade: {self.velocidade}")
    return modificar_acao

class Peixe(Animal):
    def __init__(self, nome: str, comprimento: float,
                 patas: int, cor: str, ambiente: str, 
                 velocidade: float, quantidade_escama: int) -> None:
        super().__init__(nome, comprimento, patas, cor, ambiente, velocidade)

        self._quantidade_escama = quantidade_escama

    @property
    def quantidade_escama(self):
        return self._quantidade_escama
    
    @quantidade_escama.setter
    def quantidade_escama(self, quantidade_escama: int):
        self._quantidade_escama = quantidade_escama
    
    @relatorio_peixe
    def dados(self):
        ...


if __name__ == "__main__":
    peixe = Peixe('tambaqui',10, 0, 'azul', 'aquatico', 5, 100)
    peixe.dados()
