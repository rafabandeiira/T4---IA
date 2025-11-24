from typing import Tuple
from .minimax import minimax_move


def make_move(state) -> Tuple[int, int]:
    melhor_jogada = minimax_move(state, max_depth = 5, eval_func = evaluate_count)

    return melhor_jogada


def evaluate_count(state, jogador: str) -> float:

    tabuleiro = state.board.tiles
    adversario = "W" if jogador == "B" else "B"

    qtd_jogador = sum(linha.count(jogador) for linha in tabuleiro)
    qtd_adversario = sum(linha.count(adversario) for linha in tabuleiro)

    return qtd_jogador - qtd_adversario
