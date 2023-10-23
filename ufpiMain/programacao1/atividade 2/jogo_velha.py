# Função para imprimir o tabuleiro
from typing import List
def get_tabuleiro(tabuleiro=None) -> str:
    if tabuleiro is None:
        #tabuleiro = [[" "]*3 for _ in range(3)]
        tabuleiro = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

    for linha in tabuleiro:
        print(" | ".join(linha))  # adicionando | linhas
        print("=" * 10)  # divisorias
    return tabuleiro

def verificacao_vitoria(tabuleiro, jogador)-> bool:
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador:
            return True
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador:
            return True

    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False


def verificacao_empate(tabuleiro)-> bool:
    for linha in tabuleiro:
        if " " in linha:
            return False
    return True

def conferir_entrada(entrada: str)->int:
    while True:
        try:
            valor_entrada = int(input(entrada))
            return valor_entrada
        except ValueError:
            print('tipo de valor inválido!! digite um número inteiro')

def preecher_tabuleiro() -> str:
    jogo_ativo:bool = True
    jogador_atual:str = 'X'
    tabuleiro:str = get_tabuleiro()
    linhas_disponiveis:List[int] = [0,1,2]
    colunas_disponiveis:List[int] = [0,1,2]

    while jogo_ativo:
        print(f'vez do jogador {jogador_atual.replace(jogador_atual,f"-> {jogador_atual}")}')
        linha:int = conferir_entrada(("digite a linha (0, 1 ou 2): "))
        coluna:int = conferir_entrada(("digite a coluna (0, 1 ou 2): "))

        if linha not in linhas_disponiveis or coluna not in colunas_disponiveis or\
        tabuleiro[linha][coluna] != " ":
            print("jogada invalida")
            get_tabuleiro(tabuleiro)
            continue

        tabuleiro[linha][coluna] = jogador_atual
        get_tabuleiro(tabuleiro)

        if verificacao_vitoria(tabuleiro, jogador_atual):
            jogo_ativo = False
            print(f"O jogador {jogador_atual} venceu!")
        
        elif verificacao_empate(tabuleiro):
            jogo_ativo = False
            get_tabuleiro(tabuleiro)
            print("empate")

        if jogador_atual == 'X':
            jogador_atual = 'O'
        else:
            jogador_atual = 'X'

if __name__ == "__main__":
    preecher_tabuleiro()
