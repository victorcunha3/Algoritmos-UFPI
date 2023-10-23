import random

def jogo_main():
    numero_aleatorio = random.randint(1, 100)
    print(numero_aleatorio)
    
    jogo_ativo:bool = True
    numero_minimo:int = 1
    numero_maximo:int= 100
    tentativas:int = 0
    max_tentativas:int = 99

    print(f"o numero secreto está entre {numero_minimo} e {numero_maximo}.")

    while jogo_ativo and tentativas < max_tentativas:
        solicita_numero:int = int(input('Digite um número: '))
        tentativas += 1

        if solicita_numero < numero_aleatorio:
            print("tente novamente. O numero secreto e maior")
            #numero_minimo = solicita_numero + 1
        elif solicita_numero > numero_aleatorio:
            print("tente novamente. O numero secreto e menor")
            #numero_maximo = solicita_numero - 1
        else:
            print(f"okay!!! Voce acertou e perdeu -> o número secreto: {numero_aleatorio}")
            break

    if tentativas >= max_tentativas:
        print(f"voce venceu. O numero secreto era: {numero_aleatorio}.")

    jogar_novamente:str = input('quer jogar novamente? (s/n): ').lower()
    if jogar_novamente == 's':
        jogo_main()

if __name__ == "__main__":
    jogo_main()
