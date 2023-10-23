from typing import List

def get_tabuleiro(tabuleiro: List[List[str]]) -> str:
    tabuleiroFinal: str = ""
    for linha_tabuleiro in tabuleiro:
        tabuleiroFinal += " | ".join(linha_tabuleiro)
        tabuleiroFinal += "\n"
        tabuleiroFinal += "=" * 10 + "\n"

    return tabuleiroFinal

def conferir_entrada(entrada: str) -> int:
    while True:
        try:
            valor_entrada: int = int(input(entrada))
            return valor_entrada
        except ValueError:
            print('tipo de valor inválido!! digite um número inteiro')

def jogada_valida(tabuleiro: List[List[str]],
                numero_escolhido: int) -> bool:
    jogadas_validas: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    if numero_escolhido in jogadas_validas:
        linha_tabuleiro = (numero_escolhido - 1) // 3
        coluna_tabuleiro = (numero_escolhido - 1) % 3
        if tabuleiro[linha_tabuleiro][coluna_tabuleiro] == " ":
            return True
    return False

def realizar_jogada(tabuleiro: List[List[str]],
                    numero_escolhido: int,
                    jogador_atual: str):
    linha_tabuleiro = (numero_escolhido - 1) // 3
    coluna_tabuleiro = (numero_escolhido - 1) % 3
    tabuleiro[linha_tabuleiro][coluna_tabuleiro] = jogador_atual

def verificar_vitoria(tabuleiro: List[List[str]],
                       jogador_atual: str) -> bool:
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] == jogador_atual:
            return True
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador_atual:
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador_atual:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador_atual:
        return True
    return False

def verificar_empate(tabuleiro: List[List[str]]) -> bool:
    for linha in tabuleiro:
        for posicao in linha:
            if posicao == " ":
                return False
    return True

def trocar_jogador(jogador_atual: str) -> str:
    if jogador_atual == 'X':
        proximo_jogador = 'O'
    else:
        proximo_jogador = 'X'
    
    return proximo_jogador

def preencher_tabuleiro():
    jogo_ativo = True
    jogador_atual = 'X'
    tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    print(get_tabuleiro(tabuleiro))

    while jogo_ativo:
        print(f'vez do jogador: {jogador_atual}')
        numero = conferir_entrada("digite o número da célula (1 a 9): ")

        if not jogada_valida(tabuleiro, numero):
            print("jogada inválida... Tente novamente.")
            continue

        realizar_jogada(tabuleiro, numero, jogador_atual)
        print(get_tabuleiro(tabuleiro))

        if verificar_vitoria(tabuleiro, jogador_atual):
            jogo_ativo = False
            print(f"o jogador {jogador_atual} venceu!!!")
        elif verificar_empate(tabuleiro):
            jogo_ativo = False
            print("empate!!!")

        jogador_atual = trocar_jogador(jogador_atual)

if __name__ == "__main__":
    preencher_tabuleiro()
    #print(get_tabuleiro())
