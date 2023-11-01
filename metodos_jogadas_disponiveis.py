def realizarJogada(tabuleiro, linha, coluna, jogador):
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = jogador