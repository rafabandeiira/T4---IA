import math
import random
from typing import Tuple, Callable



def minimax_move(state, max_depth: int, eval_func: Callable) -> Tuple[int, int]:

    jogador_raiz = state.player

    # -------------------------------------------------------------------------
    # Função interna recursiva da poda alfa-beta
    # -------------------------------------------------------------------------
    def alfa_beta(estado, profundidade, alfa, beta, maximiza):
        # Caso terminal ou limite atingido
        if estado.is_terminal() or (max_depth != -1 and profundidade == max_depth):
            return eval_func(estado, jogador_raiz)

        acoes = estado.get_actions()

        # Situação possível no Othello: jogador sem ações
        if not acoes:
            return eval_func(estado, jogador_raiz)

        # ---------------------------------------------------------------------
        # Nível Maximizador
        # ---------------------------------------------------------------------
        if maximiza:
            melhor_valor = -math.inf
            for acao in acoes:
                estado_filho = estado.sucessor(acao)
                valor = alfa_beta(estado_filho, profundidade + 1, alfa, beta, False)

                if valor > melhor_valor:
                    melhor_valor = valor

                if melhor_valor > alfa:
                    alfa = melhor_valor

                # Poda beta
                if beta <= alfa:
                    break

            return melhor_valor

        # ---------------------------------------------------------------------
        # Nível Minimizador
        # ---------------------------------------------------------------------
        else:
            pior_valor = math.inf
            for acao in acoes:
                estado_filho = estado.sucessor(acao)
                valor = alfa_beta(estado_filho, profundidade + 1, alfa, beta, True)

                if valor < pior_valor:
                    pior_valor = valor

                if pior_valor < beta:
                    beta = pior_valor

                # Poda alfa
                if beta <= alfa:
                    break

            return pior_valor

    # -------------------------------------------------------------------------
    # Escolha da ação no nível raiz
    # -------------------------------------------------------------------------
    melhor_jogada = None
    melhor_avaliacao = -math.inf

    for acao in state.get_actions():
        proximo_estado = state.sucessor(acao)
        avaliacao = alfa_beta(proximo_estado, 1, -math.inf, math.inf, False)

        if avaliacao > melhor_avaliacao:
            melhor_avaliacao = avaliacao
            melhor_jogada = acao

    return melhor_jogada
