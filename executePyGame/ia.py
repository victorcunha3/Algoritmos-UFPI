
  # Fução para criar tabuleiro vazio
# Função para criar tabuleiro vazio
def criaTabuleiro():
    return [' '] * 9

# Função para Exibir o tabuleiro
def imprimeTabuleiro(tabuleiro):
    print('   1   2   3')
    for i in range(3):
        row = tabuleiro[i * 3:(i + 1) * 3]
        row = ['X' if x == 'x' else 'O' if x == 'o' else ' ' for x in row]
        print(f'{i + 1} {" | ".join(row)}')

  # Função que testa se é um nó terminal
  # 0 -> não é terminal
  # 1 -> vitória de min [o]
  # 2 -> empate
  # 3 -> vitória de max [x] 
def testeTerminal(tabuleiro):
    # Testa diagonais
    if tabuleiro[0] == tabuleiro[4] == tabuleiro[8]:
        if tabuleiro[0] == 'x':
            return 3
        elif tabuleiro[0] == 'o':
            return 1
    if tabuleiro[2] == tabuleiro[4] == tabuleiro[6]:
        if tabuleiro[2] == 'x':
            return 3
        elif tabuleiro[2] == 'o':
            return 1

    # Testa linhas e colunas
    for i in range(3):
        if tabuleiro[i] == tabuleiro[i + 3] == tabuleiro[i + 6]:
            if tabuleiro[i] == 'x':
                return 3
            elif tabuleiro[i] == 'o':
                return 1
        if tabuleiro[i * 3] == tabuleiro[i * 3 + 1] == tabuleiro[i * 3 + 2]:
            if tabuleiro[i * 3] == 'x':
                return 3
            elif tabuleiro[i * 3] == 'o':
                return 1

    # Testa a ocorrência do empate
    if ' ' not in tabuleiro:
        return 2

    # Não é terminal
    return 0

def acaoMax(tabuleiro):
    # Verifica se é terminal e, caso seja, retorna utilidade e estado terminal
    terminal = testeTerminal(tabuleiro)
    if terminal:
        return [terminal, tabuleiro]
    # Criação da lista de ações possíveis
    acoes = []
    for i in range(9):
        if tabuleiro[i] == ' ':
            copia = list(tabuleiro)
            copia[i] = 'x'
            acoes.append([0, copia])
    # Para cada ação, "passa" a jogada para Min
    for i in range(len(acoes)):
        acoes[i][0] = acaoMin(acoes[i][1])[0]  # Usa a utilidade retornada
    # Retorna a melhor ação para Max
    return max(acoes)

# Função para Min
def acaoMin(tabuleiro):
    # Verifica se é terminal e, caso seja, retorna utilidade e estado terminal
    terminal = testeTerminal(tabuleiro)
    if terminal:
        return [terminal, tabuleiro]
    # Criação da lista de ações possíveis
    acoes = []
    for i in range(9):
        if tabuleiro[i] == ' ':
            copia = list(tabuleiro)
            copia[i] = 'o'
            acoes.append([0, copia])
    # Para cada ação, "passa" a jogada para Max
    for i in range(len(acoes)):
        acoes[i][0] = acaoMax(acoes[i][1])[0]
    # Retorna a melhor ação para Min
    return min(acoes)

  # Função Principal
# Função Principal
def principal():
    cpuPrimeiro = True
    while True:
        print('1-CPU 1 x CPU 2\n2-Jogador x CPU\n3-Jogador 1 x Jogador 2')
        op = int(input('4-Sair\nOpção: '))
        vezCPU = True
        if op >= 1 and op <= 3:
            while True:
                tabuleiro = criaTabuleiro()
                imprimeTabuleiro(tabuleiro)
                vezPrimeiro = True
                while not testeTerminal(tabuleiro):
                    if vezCPU and (op == 1 or op == 2):
                        if vezPrimeiro and cpuPrimeiro:
                            aux = acaoMax(tabuleiro)
                            tabuleiro = aux[1]
                        elif not vezPrimeiro:
                            aux = acaoMin(tabuleiro)
                            tabuleiro = aux[1]
                    if op == 2 and not vezCPU or op == 3:
                        while True:
                            if vezPrimeiro and (op == 3 or not cpuPrimeiro):
                                print('Jogador [x]: ')
                                valor = 'x'
                            else:
                                print('Jogador [o]: ')
                                valor = 'o'
                            posicao = int(input('Escolha uma posição de 1 a 9: '))
                            if posicao > 0 and posicao < 10:
                                if tabuleiro[posicao - 1] == ' ':
                                    tabuleiro[posicao - 1] = valor
                                    break
                    if op == 2:
                        vezCPU = not vezCPU
                    imprimeTabuleiro(tabuleiro)
                    vezPrimeiro = not vezPrimeiro
                if op == 2:
                    cpuPrimeiro = not cpuPrimeiro
                else:
                    cpuPrimeiro = True
                vezCPU = cpuPrimeiro

                resultado = testeTerminal(tabuleiro)
                if resultado == 1:
                    print('Vitória do [o]!')
                elif resultado == 3:
                    print('Vitória do [x]!')
                else:
                    print('Empate!')
                while True:
                    saida = input('Jogar novamente?[sim ou não]')
                    saida = saida.lower()
                    if saida == 'sim' or saida == 'não':
                        break
                if saida == 'não':
                    break
        else:
            return

# Execução do programa
principal()