import pygame
BLACK = (0, 0, 0)
WHITE = (100, 255, 255)
LINE_COLOR = (44, 200, 80)
BACKGROUND_COLOR = (0, 0, 0)
TEXT_COLOR = (255, 255, 255)

pygame.init()

LARGURA, ALTURA = 300, 300
TAMANHO_TELA = (LARGURA, ALTURA)
TAMANHO_CELULA = LARGURA // 3

tela_principal = pygame.display.set_mode(TAMANHO_TELA)
pygame.display.set_caption("Jogo da Velha")

"""def criarTabuleiro(janela):
    tabuleiro = []
    for i in range(3):
        linha = []
        for j in range(3):
            celula = pygame.Rect(i * TAMANHO_CELULA, j * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA)
            linha.append(celula)
            pygame.draw.rect(janela, WHITE, celula, 1)
        tabuleiro.append(linha)
    return tabuleiro"""

def realizarJogada(tabuleiro, linha, coluna, jogador):
    if tabuleiro[linha][coluna] is None:
        tabuleiro[linha][coluna] = jogador

def verificar_vitoria(tabuleiro, jogador):
    for linha in range(3):
        if all(tabuleiro[linha][coluna] == jogador for coluna in range(3)):
            return True
    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == jogador for linha in range(3)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True

    return False

def verificar_empate(tabuleiro):
    return all(tabuleiro[linha][coluna] is not None for linha in range(3) for coluna in range(3))

def minimax(tabuleiro, profundidade, maximizando, alpha, beta):
    jogador_max = "O"  # IA
    jogador_min = "X"  # Jogador humano

    if verificar_vitoria(tabuleiro, jogador_max):
        return 1
    if verificar_vitoria(tabuleiro, jogador_min):
        return -1
    if verificar_empate(tabuleiro):
        return 0

    if maximizando:
        melhor_pontuacao = -float("inf")
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] is None:
                    tabuleiro[i][j] = jogador_max
                    pontuacao = minimax(tabuleiro, profundidade + 1, False, alpha, beta)
                    tabuleiro[i][j] = None
                    melhor_pontuacao = max(pontuacao, melhor_pontuacao)
                    alpha = max(alpha, melhor_pontuacao)
                    if beta <= alpha:
                        break
        return melhor_pontuacao
    else:
        melhor_pontuacao = float("inf")
        for i in range(3):
            for j in range(3):
                if tabuleiro[i][j] is None:
                    tabuleiro[i][j] = jogador_min
                    pontuacao = minimax(tabuleiro, profundidade + 1, True, alpha, beta)
                    tabuleiro[i][j] = None
                    melhor_pontuacao = min(pontuacao, melhor_pontuacao)
                    beta = min(beta, melhor_pontuacao)
                    if beta <= alpha:
                        break
        return melhor_pontuacao

def melhor_movimento(tabuleiro):
    jogador_max = "O"  # IA
    melhor_pontuacao = -float("inf")
    melhor_movimento = None
    alpha = -float("inf")
    beta = float("inf")

    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] is None:
                tabuleiro[i][j] = jogador_max
                pontuacao = minimax(tabuleiro, 0, False, alpha, beta)
                tabuleiro[i][j] = None
                if pontuacao > melhor_pontuacao:
                    melhor_pontuacao = pontuacao
                    melhor_movimento = (i, j)
                alpha = max(alpha, melhor_pontuacao)
                if beta <= alpha:
                    break

    return melhor_movimento

def mensagemPersonalizada(mensagem):
    font = pygame.font.Font(None, 20)
    texto = font.render(mensagem, True, TEXT_COLOR)
    largura_texto, altura_texto = texto.get_size()
    
    fundo = pygame.Surface((largura_texto + 20, altura_texto + 20))
    fundo.fill(BACKGROUND_COLOR)
    tela_principal.blit(fundo, (40, ALTURA // 2 - 10))
    tela_principal.blit(texto, (50, ALTURA // 2))

def main():
    tabuleiro = [[None, None, None] for _ in range(3)]
    jogador_atual = 'X'
    vitoria_ia = False
    vitoria_jogador = False
    reiniciar = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if jogador_atual == 'X' and not vitoria_ia and not verificar_empate(tabuleiro):
                    x, y = event.pos
                    coluna, linha = x // TAMANHO_CELULA, y // TAMANHO_CELULA
                    if tabuleiro[linha][coluna] is None:
                        realizarJogada(tabuleiro, linha, coluna, jogador_atual)
                        jogador_atual = 'O'

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reiniciar = True

        if reiniciar:
            tabuleiro = [[None, None, None] for _ in range(3)]
            jogador_atual = 'X'
            vitoria_ia = False
            vitoria_jogador = False
            reiniciar = False
            tela_principal.fill(BLACK)

        if jogador_atual == 'O' and not vitoria_jogador and not verificar_empate(tabuleiro):
            linha, coluna = melhor_movimento(tabuleiro)
            realizarJogada(tabuleiro, linha, coluna, jogador_atual)
            jogador_atual = 'X'

        tela_principal.fill(BLACK)

        for linha in range(3):
            for coluna in range(3):
                celula = pygame.Rect(coluna * TAMANHO_CELULA, linha * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA)
                pygame.draw.rect(tela_principal, WHITE, celula, 1)
                if tabuleiro[linha][coluna] is not None:
                    font = pygame.font.Font(None, 100)
                    texto = font.render(tabuleiro[linha][coluna], True, WHITE)
                    tela_principal.blit(texto, (coluna * TAMANHO_CELULA + 30, linha * TAMANHO_CELULA + 30))

        if verificar_vitoria(tabuleiro, 'X'):
            mensagemPersonalizada("Você venceu! ( R para REINICIAR )")
            vitoria_jogador = True
        elif verificar_vitoria(tabuleiro, 'O'):
            mensagemPersonalizada("A IA venceu! ( R para REINICIAR )")
            vitoria_ia = True
        elif verificar_empate(tabuleiro):
            mensagemPersonalizada("Empate! ( R para REINICIAR )")

        pygame.display.update()

if __name__ == "__main__":
    main()
