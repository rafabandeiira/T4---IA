import random
import time
from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move


EVAL_TEMPLATE = [
    [100, -30, 6, 2, 2, 6, -30, 100],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [6, 1, 1, 1, 1, 1, 1, 6],
    [2, 1, 1, 3, 3, 1, 1, 2],
    [2, 1, 1, 3, 3, 1, 1, 2],
    [6, 1, 1, 1, 1, 1, 1, 6],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [100, -30, 6, 2, 2, 6, -30, 100],
]


def make_move(state) -> Tuple[int, int]:

    melhor_jogada = minimax_move(state, max_depth = 5, eval_func = evaluate_custom)

    return melhor_jogada


def evaluate_custom(state, jogador: str) -> float:

    tabuleiro = state.board.tiles
    adversario = "W" if jogador == "B" else "B"

    qtd_jogador = sum(linha.count(jogador) for linha in tabuleiro)
    qtd_adversario = sum(linha.count(adversario) for linha in tabuleiro)
    diferenca_pecas = qtd_jogador - qtd_adversario

    jogador_original = state.player

    state.player = jogador
    movimentos_jogador = len(state.legal_moves())

    state.player = adversario
    movimentos_adversario = len(state.legal_moves())

    state.player = jogador_original

    mobilidade = movimentos_jogador - movimentos_adversario

    cantos = [(0, 0), (0, 7), (7, 0), (7, 7)]
    valor_cantos = 0

    for y, x in cantos:
        if tabuleiro[y][x] == jogador:
            valor_cantos += 25
        elif tabuleiro[y][x] == adversario:
            valor_cantos -= 25

    valor_posicional = 0

    for y in range(8):
        for x in range(8):
            peso = EVAL_TEMPLATE[y][x]
            if tabuleiro[y][x] == jogador:
                valor_posicional += peso
            elif tabuleiro[y][x] == adversario:
                valor_posicional -= peso

    return (
        1.0 * diferenca_pecas
        + 2.0 * mobilidade
        + 3.0 * valor_cantos
        + 0.5 * valor_posicional
    )
