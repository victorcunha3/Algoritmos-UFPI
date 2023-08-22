"""Ler 3 valores (A, B e C) representando as medidas dos lados de um triângulo e escrever se formam 
ou não umtriângulo. OBS: para formar um triângulo, o valor de cada lado deve ser menor que a soma dos 
outros 2 lados."""

def main():
    valor_a = float(conferir_entrada("Valor para lado A: "))
    valor_b = float(conferir_entrada("Valor para lado B: "))
    valor_c = float(conferir_entrada("Valor para lado C: "))
    calculo_triangulo = triangulo(valor_a, valor_b, valor_c)
    print(calculo_triangulo)

def conferir_entrada(entrada: str) -> float:
    while True:
        try:
            valor_entrada = float(input(entrada))
            return valor_entrada
        except ValueError:
            print('tipo de valor inválido!! adicione um número')


def triangulo(A: float, B: float, C: float) -> float:
    if A < B + C and B < A + C and C < A + B:
        return("é um triângulo")
    else:
        return("não é um triângulo")

main()