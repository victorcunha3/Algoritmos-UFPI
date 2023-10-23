"""A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que
trabalhar mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular 
com um acréscimo de 50%. Escreva um algoritmo que leia onúmero de horas trabalhadas em
um mês, o salário por hora e escreva o salário total do funcionário, que deverá seracrescido 
das horas extras, caso tenham sido trabalhadas (considere que o mês possua 4 semanas exatas)."""

def main():
    horas_mes = int(conferir_entrada("digite a quantidade de horas trabalhadas/h: "))
    salario_hora = float(conferir_entrada("salario por hora: "))
    calculo_salario = salario_total(horas_mes, salario_hora)
    print(calculo_salario)

def conferir_entrada(entrada: str)->float:
    while True:
        try:
            valor_entrada = float(input(entrada))
            return valor_entrada
        except ValueError:
            print('tipo de valor inválido!! digite um número válido')

def salario_total(horas_mes: int, salario_hora: float) -> float:
    salario_final = horas_mes * salario_hora
    #horario_regular = 160
    if horas_mes > 160:
        #salario_extra = salario_final + (1.5 * salario_hora)
        hora_extra = horas_mes - 160
        salario_extra = hora_extra * (salario_hora * 1.5)
        salario_final = (160 * salario_hora) + salario_extra
    else:
        salario_final = salario_final

    return salario_final

main()