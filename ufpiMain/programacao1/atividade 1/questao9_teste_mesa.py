def main():
    teste_mesa(3, 2)
    teste_mesa(150, 3)
    teste_mesa(7, -1)
    teste_mesa(-2, 5)
    teste_mesa(50, 3)

def teste_mesa(x: int, y: int):
    z = (x * y) + 5

    if z <= 0:
        resposta = 'A'
    else:
        if z <= 100:
            resposta = 'B'
        else:
            resposta = 'C'

    print(f"z: {z}, resposta: {resposta}")

main()