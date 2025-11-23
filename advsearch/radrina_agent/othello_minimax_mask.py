import random
from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move


# mask template adjusted from https://web.fe.up.pt/~eol/IA/MIA0203/trabalhos/Damas_Othelo/Docs/Eval.html
# could optimize for symmetries but just put all values here for coding speed :P
# DO NOT CHANGE! 
EVAL_TEMPLATE = [
    [100, -30, 6, 2, 2, 6, -30, 100],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [  6,   1, 1, 1, 1, 1,   1,   6],
    [  2,   1, 1, 3, 3, 1,   1,   2],
    [  2,   1, 1, 3, 3, 1,   1,   2],
    [  6,   1, 1, 1, 1, 1,   1,   6],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [100, -30, 6, 2, 2, 6, -30, 100]
]


def make_move(state) -> Tuple[int, int]:

    inicio = time.perf_counter()
    LIMITE_TEMPO = 5.0

    melhor_jogada = None
    profundidade = 1

    while True:
        tempo_decorrido = time.perf_counter() - inicio
        if tempo_decorrido >= LIMITE_TEMPO:
            break

        jogada = minimax_move(
            state,
            max_depth=profundidade,
            eval_func=evaluate_mask
        )

        if jogada is not None:
            melhor_jogada = jogada

        profundidade += 1

        # Evita profundidades muito custosas
        if profundidade > 10:
            break

    return melhor_jogada


def evaluate_mask(state, jogador: str) -> float:

    tabuleiro = state.board.tiles
    adversario = 'W' if jogador == 'B' else 'B'

    pontuacao = 0

    for y in range(8):
        for x in range(8):
            valor_posicao = EVAL_TEMPLATE[y][x]

            if tabuleiro[y][x] == jogador:
                pontuacao += valor_posicao
            elif tabuleiro[y][x] == adversario:
                pontuacao -= valor_posicao

    return pontuacao
