"""Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor 
correspondenteem graus Celsius."""

def main():
    temperatura_fahrenheit = float(conferir_entrada("Temperatura em graus Fahrenheit: "))
    calculo_tranformacao = conversao(temperatura_fahrenheit)
    print(f'correspondente em graus Celsius: {calculo_tranformacao:.1f}')

def conferir_entrada(entrada: str)->float:
    while True:
        try:
            valor_entrada = float(input(entrada))
            return valor_entrada
        except ValueError:
            print('tipo de valor inválido!! adicione um número')

def conversao(temperatura_fahrenheit: float) -> float:
    #°C = (°F − 32) ÷ 1, 8
    graus_celsius = (temperatura_fahrenheit - 32) / 1.8
    return graus_celsius

main()