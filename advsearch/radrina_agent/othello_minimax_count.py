import random
import time
from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move


def make_move(state) -> Tuple[int, int]:

    inicio = time.perf_counter()
    LIMITE_TEMPO = 5.0

    melhor_jogada = None
    profundidade = 1

    # Aprofundamento iterativo até estourar o tempo ou o limite prático
    while True:
        tempo_decorrido = time.perf_counter() - inicio
        if tempo_decorrido >= LIMITE_TEMPO:
            break

        jogada_atual = minimax_move(state, max_depth=profundidade, eval_func=evaluate_count)

        # Se o Minimax conseguiu encontrar uma jogada válida nessa profundidade:
        if jogada_atual is not None:
            melhor_jogada = jogada_atual

        profundidade += 1

        # Evita que o Minimax tente profundidades muito altas e desperdice tempo
        if profundidade > 10:
            break

    return melhor_jogada


def evaluate_count(state, jogador: str) -> float:

    tabuleiro = state.board.tiles
    adversario = 'W' if jogador == 'B' else 'B'

    qtd_jogador = sum(linha.count(jogador) for linha in tabuleiro)
    qtd_adversario = sum(linha.count(adversario) for linha in tabuleiro)

    return qtd_jogador - qtd_adversario
