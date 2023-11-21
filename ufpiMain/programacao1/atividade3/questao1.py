x1 = float(input())
x2 = float(input())
funcao = input()

n_retangulos = 3000

largura_retagulo = (x2 - x1) / n_retangulos
area_total = 0

for retangulo in range(n_retangulos):
    x = x1 + retangulo * largura_retagulo
    altura = eval(funcao.replace('x', str(x)))
    area_retangulo = largura_retagulo * altura
    area_total += area_retangulo
    print(area_total)
