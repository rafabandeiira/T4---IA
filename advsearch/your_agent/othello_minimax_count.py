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


def make_move(state) -> Tuple[int, int]:
    start = time.perf_counter()
    TIME_LIMIT = 5.0

    best_move = None
    depth = 1
    while True:
        if time.perf_counter() - start > TIME_LIMIT:
            break
        move = minimax_move(state, max_depth=depth, eval_func=evaluate_count)
        if move is not None:
            best_move = move
        depth += 1
        if depth > 10:
            break
    return best_move


def evaluate_count(state, player:str) -> float:

    board = state.board.tiles
    opponent = 'B' if player == 'W' else 'W'

    count_player = sum(row.count(player) for row in board)
    count_opponent = sum(row.count(opponent) for row in board)

    return count_player - count_opponent
