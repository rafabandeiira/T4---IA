import math
from typing import Callable, Tuple


def minimax_move(state, max_depth: int, eval_func: Callable) -> Tuple[int, int]:

    jogador_raiz = state.player

    def MAX(s, alfa, beta, profundidade):

        if s.is_terminal() or (max_depth != -1 and profundidade == max_depth):
            return eval_func(s, jogador_raiz), None

        v = -math.inf
        melhor_acao = None

        for acao in s.legal_moves():
            s_linha = s.next_state(acao)

            v_linha, _ = MIN(s_linha, alfa, beta, profundidade + 1)

            if v_linha > v:
                v = v_linha
                melhor_acao = acao

            alfa = max(alfa, v)

            if alfa >= beta:
                break

        return v, melhor_acao

    def MIN(s, alfa, beta, profundidade):

        if s.is_terminal() or (max_depth != -1 and profundidade == max_depth):
            return eval_func(s, jogador_raiz), None

        v = math.inf
        melhor_acao = None

        for acao in s.legal_moves():
            s_linha = s.next_state(acao)

            v_linha, _ = MAX(s_linha, alfa, beta, profundidade + 1)

            if v_linha < v:
                v = v_linha
                melhor_acao = acao

            beta = min(beta, v)

            if beta <= alfa:
                break

        return v, melhor_acao

    _, melhor_acao = MAX(state, -math.inf, math.inf, 0)
    return melhor_acao
