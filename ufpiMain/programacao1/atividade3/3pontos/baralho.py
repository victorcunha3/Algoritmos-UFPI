"""As cartas de um jogo de baralho possuem naipes e valores.
Os naipes podem ser: ouro, paus, copas e espadas.
Os valores podem ser: A, 2, 3, 4, 5, 6, 7, 8, 9, J, Q, K.

Desenvolva um programa que distribui ALEATORIAMENTE as cartas de um baralho para N jogadores.

O programa deve perguntar:
 A) quantidade de jogadores
 B) quantidade de cartas para cada jogador

Exigências:
1) Não pode haver cartas repetidas;
2) Todos os jogadores devem obrigatoriamente receber a mesma quantidade de cartas.
3) Imprimir as cartas que cada jogador recebeu.
4) Imprimir as cartas que não foram distribuídas."""

import random
import pprint

def baralho():
    NAIPES = ['ouro', 'paus', 'copas', 'espadas']
    VALORES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']
    cartas = []
    for naipe_atual in NAIPES:
        for valor_atual in VALORES:
            cartas.append((naipe_atual, valor_atual))
    return cartas

def distribuir(cartas, qtd_jogadores, qtd_cartas):
    while len(cartas) < qtd_jogadores * qtd_cartas:
        try:
            qtd_cartas = int(input(f"!!!ERRO!!! nao há cartas suficientes. Insira uma quantidade de cartas válidas: "))
        except ValueError:
            print("!!!ERRO!!! insira um numero inteiro válido.")
            continue
    cartas_enviadas = {}
    cartas_resto = []
    for jogador_atual in range(qtd_jogadores):
        cartas_enviadas[jogador_atual] = []
        for _ in range(qtd_cartas):
            carta = random.choice(cartas)
            cartas_enviadas[jogador_atual].append(carta)
            cartas.remove(carta)
    cartas_resto = cartas
    return cartas_enviadas, cartas_resto

if __name__ == "__main__":
    qtd_jogadores = int(input("digite a quantidade de jogadores: "))
    qtd_cartas = int(input("digite a quantidade de cartas por jogador: "))
    cartas = baralho()
    #print(cartas)
    cartas_distribuidas, cartas_restantes = distribuir(cartas, qtd_jogadores, qtd_cartas)
    print("-------CARTAS DISTRIBUÍDAS-------")
    pprint.pprint(cartas_distribuidas)
    print("-------CARTAS QUE SOBRARAM-------")
    pprint.pprint(cartas_restantes)