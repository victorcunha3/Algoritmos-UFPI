import random
from typing import List
from arquivo_dicas import dicas_palavras

def sortear_palavra():
    palavra:str = random.choice(list(dicas_palavras.keys()))
    dica:str = dicas_palavras[palavra]
    return palavra, dica

def get_palavra_oculta(palavra:str, letras_corretas:str):
    palavra_oculta:str = ''
    for letra in palavra:
        if letra in letras_corretas:
            palavra_oculta += letra
        else:
            palavra_oculta += '#'
    return palavra_oculta

def main_jogo():
    erros_score:int = 0
    letras_corretas:List[str] = []
    palavra, dica = sortear_palavra()

    while erros_score < 5:
        print(f'Dica: {dica}')
        palavra_oculta: str = get_palavra_oculta(palavra, letras_corretas)
        print(f'Palavra: {palavra_oculta}')

        if palavra_oculta == palavra:
            print(f'parabéns!!! voce acertou a palavra: {palavra}')
            break

        letra:str = input('digite uma letra: ').lower()

        if len(letra) != 1:
            print('Por favor, digite uma única letra válida.')
            continue

        if letra in letras_corretas:
            print(f'a letra "{letra}" já foi escolhida anteriormente')
            continue

        if letra in palavra:
            letras_corretas.append(letra)
        else:
            erros_score += 1
            print(f'a letra "{letra}" nao esta na palavra -> vc errou: {erros_score}/5')

    if erros_score >= 5:
        print(f'genio!! voce nao adivinhou a palavra: {palavra}')

if __name__ == "__main__":
    main_jogo()
