from typing import List

TABULEIRO: List[List[str]] = [
            [" O ", " O ", " X "],
            [" X ", " O ", " "],
            [" X ", " X ", " X "],
        ]

def verificar_empate(tabuleiro: List[List[str]]) -> bool:
    
    for linha_atual in tabuleiro:
        if len(tabuleiro) != 3 or len(linha_atual) != 3:
            raise ValueError("o tabuleiro deve conter as dimensões -> 3x3")
        for posicao_atual in linha_atual:
            if posicao_atual == " ":
                return False
    return True


if __name__ == "__main__":
    print(verificar_empate(tabuleiro=TABULEIRO))