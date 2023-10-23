"""
Escreva uma classe em que cada objeto representa um voo que acontece em
determinada data e em determinado horário. Cada voo possui no máximo 100
passageiros, e a classe permite controlar a ocupação das vagas. A classe deve ter os
seguintes métodos:
"""
#https://docs.python.org/3/library/typing.html
from questao2_data import Data
from typing import List

class Voo:
    assentos_ocupados: List[int] = []
    def __init__(self, data: str, horario: str, numero_voo:int) -> None:
        self.data = Data(data).data
        self.horario = horario
        self.capacidade_maxima = 100
        self.numero_voo = numero_voo
    
    def proximo_livre(self):
        for i in range(1,101):
            if i not in self.assentos_ocupados:
                escolhas = i
                print(escolhas)
                break

    def verifica(self, cadeira_verificar:int):
        if cadeira_verificar < 1 or cadeira_verificar >100:
            return f'cadeiras válidas somente entre 1 e 100'
        if cadeira_verificar in self.assentos_ocupados:
            return "cadeira ocupada"
        return "cadeira livre"
    
    def vagas_disponiveis(self):
        return self.capacidade_maxima - len(self.assentos_ocupados)
    
    def ocupa(self, numero_cadeira: int):
        if numero_cadeira < 1 or numero_cadeira >100:
            return f'cadeiras válidas somente entre 1 e 100'
        if numero_cadeira in self.assentos_ocupados:
            return f'Assento {numero_cadeira} já ocupado'
        elif self.vagas_disponiveis() > 0:
                self.assentos_ocupados.append(numero_cadeira)
                return f'Aasento numero {numero_cadeira} cadastrado'
        else:
            return 'nao ha vagas disponiveis'
    
    def getVoo(self):
        return self.numero_voo
    
    def getData(self):
        return self.data
    
    def clone(self):
        objeto_clonado_numero = Voo(self.data,self.horario,self.numero_voo).numero_voo
        objeto_clonado_data = Voo(self.data,self.horario,self.numero_voo).data
        objeto_clonado_horario = Voo(self.data,self.horario,self.numero_voo).horario
        return objeto_clonado_numero, objeto_clonado_data, objeto_clonado_horario

if __name__ == "__main__":

    voo1 = Voo('22-01-2011', '10:20', 1234)
    voo2 = Voo('11-09-2011','10-20',147)
    print(voo1.vagas_disponiveis())
    print(voo1.ocupa(100))
    print(voo1.vagas_disponiveis())
    print(voo1.ocupa(10))
    print(voo1.vagas_disponiveis())
    print(voo1.assentos_ocupados)
    print(voo2.ocupa(1))
    print(voo2.vagas_disponiveis())
    voo2.proximo_livre()
    voo2.ocupa(2)
    voo2.proximo_livre()
    print(voo2.assentos_ocupados)
    print(voo2.verifica(10))
    print(voo2.getData())
    print(voo2.clone())
