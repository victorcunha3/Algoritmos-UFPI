class Animal:
    def __init__(self, nome: str, comprimento: float, patas: int, cor: str, ambiente: str, velocidade: float) -> None:
        self._nome = nome
        self._comprimento = comprimento
        self._patas = patas
        self._cor = cor
        self._ambiente = ambiente
        self._velocidade = velocidade
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome: str) -> None:
        self._nome = novo_nome
    
    @property
    def comprimento(self) -> float:
        return self._comprimento
    
    @comprimento.setter
    def comprimento(self, novo_comprimento: float) -> None:
        self._comprimento = novo_comprimento
    
    @property
    def patas(self) -> int:
        return self._patas
    
    @patas.setter
    def patas(self, novas_patas: int) -> None:
        self._patas = novas_patas
    
    @property
    def cor(self) -> str:
        return self._cor
    
    @cor.setter
    def cor(self, nova_cor: str) -> None:
        self._cor = nova_cor
    
    @property
    def ambiente(self) -> str:
        return self._ambiente
    
    @ambiente.setter
    def ambiente(self, novo_ambiente: str) -> None:
        self._ambiente = novo_ambiente
    
    @property
    def velocidade(self) -> float:
        return self._velocidade
    
    @velocidade.setter
    def velocidade(self, nova_velocidade: float) -> None:
        self._velocidade = nova_velocidade

    def dados(self) -> str:
        print(f"nome: {self.nome}")
        print(f"comprimento: {self.comprimento}")
        print(f"patas: {self.patas}")
        print(f"cor: {self.cor}")
        print(f"ambiente: {self.ambiente}")
        print(f"velocidade: {self.velocidade}")

if __name__ == '__main__':
    animal = Animal("Leão", 200, 4, "Amarelo", "Savana", 10)
    animal.dados()
