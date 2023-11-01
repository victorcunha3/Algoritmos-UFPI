import random

def imprimir_tabuleiro(tabuleiro):
    for i in range(3):
        for j in range(3):
            print(tabuleiro[i * 3 + j], end="")
            if j < 2:
                print(" | ", end="")
        print()
        if i < 2:
            print("-" * 9)

def verificar_vitoria(tabuleiro, jogador):
    for i in range(3):
        if all(casa == jogador for casa in tabuleiro[i * 3:i * 3 + 3]):
            return True

    for j in range(3):
        if all(tabuleiro[i * 3 + j] == jogador for i in range(3)):
            return True

    if all(tabuleiro[i] == jogador for i in [0, 4, 8]) or all(tabuleiro[i] == jogador for i in [2, 4, 6]):
        return True

    return False

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

def verificar_empate(tabuleiro):
    return not any(casa == " " for casa in tabuleiro)

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
        for i in range(9):
            if tabuleiro[i] == " ":
                tabuleiro[i] = jogador_max
                pontuacao = minimax(tabuleiro, profundidade + 1, False, alpha, beta)
                tabuleiro[i] = " "
                melhor_pontuacao = max(pontuacao, melhor_pontuacao)
                alpha = max(alpha, melhor_pontuacao)
                if beta <= alpha:
                    break
        return melhor_pontuacao
    else:
        melhor_pontuacao = float("inf")
        for i in range(9):
            if tabuleiro[i] == " ":
                tabuleiro[i] = jogador_min
                pontuacao = minimax(tabuleiro, profundidade + 1, True, alpha, beta)
                tabuleiro[i] = " "
                melhor_pontuacao = min(pontuacao, melhor_pontuacao)
                beta = min(beta, melhor_pontuacao)
                if beta <= alpha:
                    break
        return melhor_pontuacao

def trocar_jogador(jogador_atual: str) -> str:
    if jogador_atual == 'X':
        return 'O'
    else:
        return "X"

def melhor_movimento(tabuleiro):
    jogador_max = "O"  # IA
    melhor_pontuacao = -float("inf")
    melhor_movimento = None
    alpha = -float("inf")
    beta = float("inf")

    for i in range(9):
        if tabuleiro[i] == " ":
            tabuleiro[i] = jogador_max
            pontuacao = minimax(tabuleiro, 0, False, alpha, beta)
            tabuleiro[i] = " "
            if pontuacao > melhor_pontuacao:
                melhor_pontuacao = pontuacao
                melhor_movimento = i
            alpha = max(alpha, melhor_pontuacao)
            if beta <= alpha:
                break

    return melhor_movimento


def movimento_mediano(tabuleiro):
    movimentos_disponiveis = [iter for iter in range(9) if tabuleiro[iter] == " "]

    if movimentos_disponiveis:
        return random.choice(movimentos_disponiveis)
    else:
        return None
    
def conf_jogada(tabuleiro, jogador_humano):
  while True:
    try:
        escolha = conf_entrada("Escolha uma posição (1-9): ")
        if 1 <= escolha <= 9 and tabuleiro[escolha - 1] == " ":
          tabuleiro[escolha - 1] = jogador_humano
          break
        else:
          print("Posição inválida ou ocupada. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Tente novamente.")

def jogar_contra_ia():
    while True:
        print("Bem-Vindo, vocé será o jogador [X]")
        print("Níveis de dificuldade")
        print("Digite 1 para nível impossível(IA) e 2 para nível fácil (0 para sair)")
        nivel = input("digite um nível: ")
        niveis_dificuldade = ['1', '2','0']
        if nivel in niveis_dificuldade:
            if nivel == niveis_dificuldade[0]:

                while True:
                    tabuleiro = [" " for _ in range(9)]
                    jogador_humano = "X"
                    jogador_IA = "O"

                    while True:
                        imprimir_tabuleiro(tabuleiro)

                        conf_jogada(tabuleiro, jogador_humano)

                        if verificar_vitoria(tabuleiro, jogador_humano):
                            imprimir_tabuleiro(tabuleiro)
                            print("Você venceu!")
                            break

                        if verificar_empate(tabuleiro):
                            imprimir_tabuleiro(tabuleiro)
                            print("O jogo empatou!")
                            break

                        movimento_IA = melhor_movimento(tabuleiro)
                        tabuleiro[movimento_IA] = jogador_IA

                        if verificar_vitoria(tabuleiro, jogador_IA):
                            imprimir_tabuleiro(tabuleiro)
                            print("A IA venceu!")
                            break

                    jogar_novamente = input("Deseja jogar novamente? (s/n): ")
                    if jogar_novamente.lower() != "s":
                        break
            elif nivel == niveis_dificuldade[1]:
                while True:
                    tabuleiro = [" " for _ in range(9)]
                    jogador_humano = "X"
                    jogador_IA = "O"

                    while True:
                        imprimir_tabuleiro(tabuleiro)

                        conf_jogada(tabuleiro, jogador_humano)

                        if verificar_vitoria(tabuleiro, jogador_humano):
                            imprimir_tabuleiro(tabuleiro)
                            print("Você venceu!")
                            break

                        if verificar_empate(tabuleiro):
                            imprimir_tabuleiro(tabuleiro)
                            print("O jogo empatou!")
                            break

                        movimento_IA = movimento_mediano(tabuleiro)
                        tabuleiro[movimento_IA] = jogador_IA

                        if verificar_vitoria(tabuleiro, jogador_IA):
                            imprimir_tabuleiro(tabuleiro)
                            print("A IA venceu!")
                            break

                    jogar_novamente = input("Deseja jogar novamente? (s/n): ")
                    if jogar_novamente.lower() != "s":
                        break
            elif nivel == niveis_dificuldade[2]:
                break
        else:
            print('nivel de dificuldade inválido')

def jogar_contra_humano():
    while True:
        tabuleiro = [" " for _ in range(9)]
        jogador1 = "X"
        jogador_atual = jogador1

        while True:
            imprimir_tabuleiro(tabuleiro)
            print(f"vez do jogador -> [{jogador_atual}]")
            while True:
                try:
                    escolha = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): "))
                    if 1 <= escolha <= 9 and tabuleiro[escolha - 1] == " ":
                        tabuleiro[escolha - 1] = jogador_atual
                        break
                    else:
                        print("Posição inválida ou ocupada. Tente novamente.")
                except ValueError:
                    print("Entrada inválida. Tente novamente.")

            if verificar_vitoria(tabuleiro, jogador_atual):
                imprimir_tabuleiro(tabuleiro)
                print(f"Jogador {jogador_atual} venceu!")
                break

            if verificar_empate(tabuleiro):
                imprimir_tabuleiro(tabuleiro)
                print("O jogo empatou!")
                break

            jogador_atual = trocar_jogador(jogador_atual)

        jogar_novamente = input("Deseja jogar novamente? (s/n): ")
        if jogar_novamente.lower() != "s":
            break


def main():
    while True:
        print("Jogo da Velha")
        print("1. Jogar contra Humano")
        print("2. Jogar contra IA")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            jogar_contra_humano()
        elif escolha == "2":
            jogar_contra_ia()
        elif escolha == "3":
            print("Obrigado por jogar!")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()