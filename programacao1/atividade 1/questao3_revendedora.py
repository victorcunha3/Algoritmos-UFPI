"""Uma revendedora de carros usados --paga a seus funcionários vendedores um salário fixo por mês, mais uma comissão 
também fixa para cada carro vendido e mais 5% do valor das vendas por ele efetuadas--. Escreva um algoritmo que leia 
o número de carros por ele vendidos, o valor total de suas vendas, o salário fixo e o valor que ele recebe por carro 
vendido. Calcule e escreva o salário final do vendedor."""

def main():
    carros_vendidos = int(conferir_entrada("quantidade de carros vendidos: "))
    valor_vendas = float(conferir_entrada("valor total de vendas: "))
    salario_fixo = float(conferir_entrada("digite o salario: "))
    valor_carro = float(conferir_entrada("valor que recebe por carro: "))

    calculo_final = salario_total_vendas(carros_vendidos, valor_vendas, salario_fixo, valor_carro)
    print(f'o salario final é: {calculo_final}')

def conferir_entrada(entrada: str)-> float:
    while True:
        try:
            valor_entrada = float(input(entrada))
            return valor_entrada
        except ValueError:
            print('tipo de valor inválido!! adicione um número')

def salario_total_vendas(carros_vendidos: int, valor_vendas: float, salario_fixo: float, valor_carro: float) -> float:
    porcentagem_sobre_carros = (5/100) * valor_vendas
    comissao_fixa_final = valor_carro * carros_vendidos
    salario_final = salario_fixo + comissao_fixa_final + porcentagem_sobre_carros
    return salario_final

main()