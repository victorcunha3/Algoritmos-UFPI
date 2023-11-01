from typing import List
from colorama import Fore, init, Style

init(autoreset=True)

def cor_tabuleiro(simbolo: str) -> str:
    if simbolo == 'X':
        return f"{Fore.YELLOW}{simbolo}{Style.RESET_ALL}"
    elif simbolo == 'O':
        return f"{Fore.MAGENTA}{simbolo}{Style.RESET_ALL}"
    else:
        return simbolo

def tabuleiro(jogo_da_velha: str):
    for i in range(3):
        linhaFinal = f" {cor_tabuleiro(jogo_da_velha[i][0])} | {cor_tabuleiro(jogo_da_velha[i][1])} | {cor_tabuleiro(jogo_da_velha[i][2])}"
        print(linhaFinal)
        if i < 2:
            print(" ==========")

def conf_entrada(entrada: str) -> int | str:
    while True:
        try:
            comand = int(input(entrada))
            if comand < 0:
                raise ValueError
        except ValueError:
            print("Digite um valor válido")
        else:
            return comand

def jogada_valida(tabuleiro: str,
                   jogada: int) -> bool:
    if jogada < 1 or jogada > 9:
        return False
    linha, coluna = (jogada - 1) // 3, (jogada - 1) % 3
    if tabuleiro[linha][coluna] != " ":
        return False
    return True

def fazer_jogada(tabuleiro: str,
                  jogada: int,
                    jogador_atual: str):
    
    linha, coluna = (jogada - 1) // 3, (jogada - 1) % 3
    tabuleiro[linha][coluna] = jogador_atual

def ganhou(tabuleiro: str) -> bool:
    for i in range(3):
        linha:str = "".join(tabuleiro[i])
        if linha == 'XXX' or linha == 'OOO':
            return True
    for i in range(3):
        coluna = tabuleiro[0][i] + tabuleiro[1][i] + tabuleiro[2][i]
        if coluna == 'XXX' or coluna == 'OOO':
            return True
    diagonal1:str = tabuleiro[0][0] + tabuleiro[1][1] + tabuleiro[2][2]
    diagonal2:str = tabuleiro[0][2] + tabuleiro[1][1] + tabuleiro[2][0]
    if diagonal1 == 'XXX' or diagonal1 == 'OOO' or diagonal2 == 'XXX' or diagonal2 == 'OOO':
        return True
    return False

def verificar_empate(tabuleiro: List[List[str]]) -> bool:
    for linha_atual in tabuleiro:
        for posicao_atual in linha_atual:
            if posicao_atual == " ":
                return False
    return True

def trocar_jogador(jogador_atual: str) -> str:
    if jogador_atual == 'X':
        return 'O'
    else:
        return "X"


def jogo_da_velha() -> str:
    jogo_da_velha: List[List[str]] = [[" ", " ", " "], 
                                      [" ", " ", " "], 
                                      [" ", " ", " "]]
    jogador_atual: str = 'X'
    jogo_ativo: bool = True
    
    while jogo_ativo:
        tabuleiro(jogo_da_velha)
        jogada_numero: int = conf_entrada(f"Vez do Jogador {jogador_atual}, escolha uma posição (1-9) ou 0 para sair: ")

        if jogada_numero == 0:
            jogo_ativo = False

        if jogada_valida(jogo_da_velha, jogada_numero):
            fazer_jogada(jogo_da_velha, jogada_numero, jogador_atual)

            if ganhou(jogo_da_velha):
                tabuleiro(jogo_da_velha)
                print(f"O jogador {jogador_atual} ganhou!")
                jogo_ativo = False

            if verificar_empate(jogo_da_velha):
                tabuleiro(jogo_da_velha)
                print("Empate!!!!")
                jogo_ativo = False

            jogador_atual = trocar_jogador(jogador_atual)
        else:
            print("Jogada inválida. Tente novamente.")


def jogo_maquina():
    mensagem:str = "FASE DE CRIAÇÃO ^-^ . VOLTE EM BREVE"
    texto_colorido:str = f"{Fore.CYAN}{Style.NORMAL}{mensagem}{Style.RESET_ALL}"
    print(texto_colorido)

def jogo_principal():
    menu_escolha: List[str] = ["1", "2", "3"]
    while True:
        mensagem_inicial:str = "Bem-vindo ao jogo da velha!"
        saudacao_cor:str = f"{Fore.LIGHTMAGENTA_EX}{Style.NORMAL}{mensagem_inicial}{Style.RESET_ALL}"
        print(saudacao_cor)
        caractere = '#'*30
        caractere_cor = f"{Fore.LIGHTYELLOW_EX}{Style.DIM}{caractere}{Style.RESET_ALL}"
        print(caractere_cor)
        print("Digite 1 para Jogar contra outro jogador")
        print("Digite 2 para Jogar contra a máquina")
        print("Digite 3 para Sair")
        print(caractere_cor)
        escolha:str = input("Escolha entre as opções (1, 2 ou 3): ")

        if escolha == menu_escolha[0]:
            jogo_da_velha()
        elif escolha == menu_escolha[1]:
            jogo_maquina()
        elif escolha == menu_escolha[2]:
            print("Você saiu do jogo. Até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente!")

if __name__ == "__main__":
    jogo_principal()