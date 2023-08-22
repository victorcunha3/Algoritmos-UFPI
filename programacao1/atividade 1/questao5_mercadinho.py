"""No mercadinho Mamão com Açucar as maçãs custam R$ 3,50 cada se forem compradas 
menos de uma dúzia, eR$ 3,00 se forem compradas pelo menos 12. Escreva um programa 
que calcule e escreva o custo total da compra."""

def main():
    quantidade = int(conferir_entrada("quantidade de maçãs: "))
    calcular_valor = calculo_duzia(quantidade)
    print(calcular_valor)

def conferir_entrada(entrada: str)->int:
    while True:
        try:
            valor_entrada = int(input(entrada))
            return valor_entrada
        except ValueError:
            print('tipo de valor inválido!! digite um numero válido sem pontos ou espaços')

def calculo_duzia(quantidade: int) -> int:
    menor_duzia = 3.50
    maior_duzia = 3.00

    if quantidade >= 12:
        custo = quantidade * maior_duzia
    
    elif quantidade < 12:
        custo = quantidade * menor_duzia
    
    return custo

main()