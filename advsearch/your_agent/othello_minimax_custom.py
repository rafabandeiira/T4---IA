import random
import time
from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.

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

    start = time.perf_counter()
    TIME_LIMIT = 5.0

    best_move = None
    depth = 1
    while True:
        if time.perf_counter() - start > TIME_LIMIT:
            break
        move = minimax_move(state, max_depth=depth, eval_func=evaluate_custom)
        if move is not None:
            best_move = move
        depth += 1
        if depth > 10:
            break
    return best_move


def evaluate_custom(state, player:str) -> float:

    board = state.board.tiles
    opponent = 'B' if player == 'W' else 'W'

    count_player = sum(row.count(player) for row in board)
    count_opponent = sum(row.count(opponent) for row in board)
    piece_diff = count_player - count_opponent

    current_player = state.player
    state.player = player
    player_moves = len(state.get_actions())
    state.player = opponent
    opponent_moves = len(state.get_actions())
    state.player = current_player
    mobility = player_moves - opponent_moves

    corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
    corner_score = 0
    for y, x in corners:
        if board[y][x] == player:
            corner_score += 25
        elif board[y][x] == opponent:
            corner_score -= 25

    mask_score = 0
    for y in range(8):
        for x in range(8):
            if board[y][x] == player:
                mask_score += EVAL_TEMPLATE[y][x]
            elif board[y][x] == opponent:
                mask_score -= EVAL_TEMPLATE[y][x]

    return 1.0 * piece_diff + 2.0 * mobility + 3.0 * corner_score + 0.5 * mask_score
