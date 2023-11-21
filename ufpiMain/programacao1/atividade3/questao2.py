import math

def ler_numeros(n):
    vetor = []
    for i in range(n):
        numero = int(input(f"digite um número ({i + 1}/{n}): "))
        vetor.append(numero)
    return vetor

def variacao(vetor):
    somatorio = 0
    for i in range(len(vetor)):
        v = vetor[i] - media(vetor)
        somatorio += v * v
    return somatorio / (len(vetor) - 1)

def media(vetor):
    return sum(vetor) / float(len(vetor))

def imprimir_resultado(variacao):
    print(f"resultado d = {math.sqrt(variacao):.2f}")

if __name__ == "__main__":
    vetor = ler_numeros(5)
    variacao = variacao(vetor)
    imprimir_resultado(variacao)
