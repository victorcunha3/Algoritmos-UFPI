from pynput import keyboard

# Posições iniciais dos jogadores
posicao_jogador1 = 0
posicao_jogador2 = 0

# Tamanho mínimo para ganhar o jogo
tamanho_minimo_ganhar = 10

# Função para imprimir a representação do jogo
def imprimir_jogo():
    print("-" * (posicao_jogador1 + 1) + "1" + "-" * (20 - posicao_jogador1))
    print("-" * (posicao_jogador2 + 1) + "2" + "-" * (20 - posicao_jogador2))

# Função para verificar quem ganhou
def verificar_ganhador():
    if posicao_jogador1 >= tamanho_minimo_ganhar:
        print("Jogador 1 ganhou!")
        return True
    elif posicao_jogador2 >= tamanho_minimo_ganhar:
        print("Jogador 2 ganhou!")
        return True
    return False

# Função chamada quando uma tecla é pressionada
def on_key_press(key):
    global posicao_jogador1, posicao_jogador2
    if key == keyboard.Key.left:
        posicao_jogador1 = max(0, posicao_jogador1 - 1)
    elif key == keyboard.Key.right:
        posicao_jogador1 = min(20, posicao_jogador1 + 1)
    elif key == keyboard.KeyCode.from_char('a'):
        posicao_jogador2 = max(0, posicao_jogador2 - 1)
    elif key == keyboard.KeyCode.from_char('d'):
        posicao_jogador2 = min(20, posicao_jogador2 + 1)

    imprimir_jogo()

    if verificar_ganhador():
        listener.stop()

# Iniciar a captura de teclas
listener = keyboard.Listener(on_press=on_key_press)
listener.start()

# Inicializa o jogo
print("Jogo de Cabo de Guerra")
imprimir_jogo()

# Aguarda o usuário encerrar o jogo
listener.join()