"""Faça um algoritmo para ler um número que é um código de usuário. Caso este código seja diferente de um 
códigoarmazenado internamente no algoritmo (igual a 1234) deve ser apresentada a mensagem 'Usuário inválido!'. 
Caso oCódigo seja correto, deve ser lido outro valor que é a senha. Se esta senha estiver incorreta 
(a certa é 9999) deve sermostrada a mensagem 'senha incorreta'. Caso a senha esteja correta, deve ser 
mostrada a mensagem 'Acesso permitido'."""

def main():
    codigo_armazenado = 1234
    senha_armazenada = 9999
    while True:
        try:
            codigo_usuario = int(input("digite o código: "))
            if codigo_usuario == codigo_armazenado:
                break
            else:
                print("usuário inválido!")
        except ValueError:
            print("entrada inválida. Digite um número inteiro.")
    while True:
        try:
            senha = int(input("Digite a senha: "))
            if senha == senha_armazenada:
                print("acesso permitido")
                break
            else:
                print("senha incorreta")
        except ValueError:
            print("entrada inválida. Digite um número inteiro.")

main()
