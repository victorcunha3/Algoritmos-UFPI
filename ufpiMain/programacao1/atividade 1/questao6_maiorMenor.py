"""Ler dois valores e informar qual deles é o maior e o menor, 
ou informar que são iguais (se for o caso)."""

def main():
    numero1 = int(conferir_entrada("Numero 1: "))
    numero2 = int(conferir_entrada("Numero 2: "))

    if numero1 > numero2:
        print(f'o numero {numero1} é o maior e o {numero2} é o menor')
    elif numero2 > numero1:
        print(f'o numero {numero2} é o maior e o {numero1} é o menor')
    elif numero1 == numero2:
        print("Ambos os numeros sao iguais")

def conferir_entrada(entrada: str)->int:
    while True:
        try:
            valor_entrada = int(input(entrada))
            return valor_entrada
        except ValueError:
            print('tipo de valor inválido!! digite um número inteiro')

main()