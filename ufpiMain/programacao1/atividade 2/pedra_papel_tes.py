import random
from typing import List
pedra_papel_tesoura:List[str] = ['pedra', 'papel', 'tesoura']

def main_jogo():
    jogo_ativo:bool = True
    while jogo_ativo:
        palavra_sorteada:str = sortear_alternativa()
        opcao_usuario:str = input("escolha entre pedra, papel ou tesoura: ")
        if opcao_usuario not in pedra_papel_tesoura:
            print("Escolha inválida. Tente novamente.")
            continue
        if opcao_usuario == palavra_sorteada:
            print(f"{palavra_sorteada} -> iguais")
        elif (opcao_usuario == "pedra" and palavra_sorteada == "tesoura") or\
            (opcao_usuario == "papel" and palavra_sorteada == "pedra") or\
            (opcao_usuario == "tesoura" and palavra_sorteada == "papel"):
            print(f"voce ganhou! {opcao_usuario} > {palavra_sorteada}")
        else:
            print(f"voce perdeu! {palavra_sorteada} > {opcao_usuario}")

        jogar_novamente:str = input("quer jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            jogo_ativo = False

def sortear_alternativa() -> str:
    palavra:str = random.choice(pedra_papel_tesoura)
    return palavra

if __name__ == "__main__":
    main_jogo()