import time
import math
from typing import Tuple
from ..othello.gamestate import GameState
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


def make_move(state: GameState) -> Tuple[int, int]:

    start_time = time.time()
    time_limit = 4.8

    best_move = None

    legal_moves = state.legal_moves()

    if not legal_moves:
        return (-1, -1)

    if len(legal_moves) == 1:
        return list(legal_moves)[0]

    depth = 1
    max_depth_possible = 64

    while depth <= max_depth_possible:
        loop_start = time.time()

        current_move = minimax_move(
            state, max_depth=depth, eval_func=evaluate_tournament
        )

        if current_move:
            best_move = current_move

        elapsed = time.time() - start_time
        loop_duration = time.time() - loop_start

        if elapsed + (loop_duration * 6) > time_limit:
            break

        depth += 1

        if elapsed > time_limit:
            break

    return best_move


def evaluate_tournament(state: GameState, jogador: str) -> float:

    tabuleiro = state.board.tiles
    adversario = "W" if jogador == "B" else "B"

    total_pecas = 0
    qtd_jogador = 0
    qtd_adversario = 0

    for y in range(8):
        row = tabuleiro[y]
        qtd_jogador += row.count(jogador)
        qtd_adversario += row.count(adversario)

    total_pecas = qtd_jogador + qtd_adversario
    diferenca_pecas = qtd_jogador - qtd_adversario

    # Contagem de pecas apenas na fase final
    w_diff = 0.0
    w_mob = 0.0
    w_corner = 0.0
    w_pos = 0.0

    if total_pecas < 20:
        w_diff = 0.5
        w_mob = 4.0
        w_corner = 5.0
        w_pos = 1.0
    elif total_pecas <= 50:
        w_diff = 1.0
        w_mob = 2.0
        w_corner = 10.0
        w_pos = 1.5
    else:  # Endgame
        w_diff = 5.0
        w_mob = 1.0
        w_corner = 15.0
        w_pos = 1.0

    # Mobilidade
    original_player = state.player

    state.player = jogador
    mob_jogador = len(state.legal_moves())

    state.player = adversario
    mob_adversario = len(state.legal_moves())

    state.player = original_player

    mobilidade = mob_jogador - mob_adversario

    # Cantos
    valor_cantos = 0
    valor_posicional = 0

    cantos_coords = [(0, 0), (0, 7), (7, 0), (7, 7)]

    for cy, cx in cantos_coords:
        peca = tabuleiro[cy][cx]
        if peca == jogador:
            valor_cantos += 1
        elif peca == adversario:
            valor_cantos -= 1

    # Cálculo posicional (matriz de pesos)
    for y in range(8):
        for x in range(8):
            peso = EVAL_TEMPLATE[y][x]
            peca = tabuleiro[y][x]
            if peca == jogador:
                valor_posicional += peso
            elif peca == adversario:
                valor_posicional -= peso

    score = (
        (w_diff * diferenca_pecas)
        + (w_mob * mobilidade)
        + (w_corner * valor_cantos * 25)
        + (w_pos * valor_posicional)
    )

    return score
