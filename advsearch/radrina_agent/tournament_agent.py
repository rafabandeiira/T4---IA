import time
import math
from typing import Tuple
from ..othello.gamestate import GameState
from .minimax import minimax_move

# Template de avaliação posicional (Matrix de Pesos)
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
    """
    Determina a melhor jogada usando Minimax com Iterative Deepening
    para respeitar o limite de tempo de 5 segundos.
    """
    start_time = time.time()
    time_limit = 4.9  # Margem de segurança (limite é 5.0s)

    best_move = None

    # Obtém jogadas legais
    legal_moves = state.legal_moves()

    # Se não houver jogadas, retorna pass (-1, -1)
    if not legal_moves:
        return (-1, -1)

    # CORREÇÃO AQUI: Converter para lista antes de acessar o índice 0
    if len(legal_moves) == 1:
        return list(legal_moves)[0]

    # Iterative Deepening
    # Começa com profundidade 1 e aumenta até onde o tempo permitir
    depth = 1
    max_depth_possible = 64  # Impossível passar disso no Othello

    while depth <= max_depth_possible:
        loop_start = time.time()

        # Chama o minimax com a profundidade atual
        current_move = minimax_move(state, max_depth=depth, eval_func=evaluate_tournament)

        # Se o minimax retornou algo válido, atualizamos nossa melhor jogada
        if current_move:
            best_move = current_move

        elapsed = time.time() - start_time
        loop_duration = time.time() - loop_start

        # Heurística de Tempo:
        # Se (tempo_atual + 6*tempo_do_ultimo_loop) > limite, paramos.
        # O fator 6 é conservador (branching factor médio)
        if elapsed + (loop_duration * 6) > time_limit:
            break

        depth += 1

        # Check extra de segurança absoluta
        if elapsed > time_limit:
            break

    return best_move


def evaluate_tournament(state: GameState, jogador: str) -> float:
    """
    Heurística customizada avançada.
    Combina: Diferença de peças, Mobilidade, Cantos e Valor Posicional.
    Os pesos variam dinamicamente conforme a fase do jogo.
    """
    tabuleiro = state.board.tiles
    adversario = "W" if jogador == "B" else "B"

    # 1. Contagem de peças e fase do jogo
    total_pecas = 0
    qtd_jogador = 0
    qtd_adversario = 0

    # Loop otimizado para leitura única do tabuleiro
    for y in range(8):
        row = tabuleiro[y]
        qtd_jogador += row.count(jogador)
        qtd_adversario += row.count(adversario)

    total_pecas = qtd_jogador + qtd_adversario
    diferenca_pecas = qtd_jogador - qtd_adversario

    # Definição de Pesos Dinâmicos baseados na fase do jogo
    # Fase 1: Abertura (< 20 peças) -> Prioriza mobilidade e posicionamento, ignora contagem
    # Fase 2: Meio (20-50 peças) -> Balanceado
    # Fase 3: Final (> 50 peças) -> Contagem de peças torna-se crucial

    w_diff = 0.0
    w_mob = 0.0
    w_corner = 0.0
    w_pos = 0.0

    if total_pecas < 20:
        w_diff = 0.5  # Contagem pouco importa agora
        w_mob = 4.0  # Mobilidade é rei no início
        w_corner = 5.0  # Cantos sempre bons
        w_pos = 1.0  # Tabuleiro posicional importante
    elif total_pecas <= 50:
        w_diff = 1.0
        w_mob = 2.0
        w_corner = 10.0
        w_pos = 1.5
    else:  # Endgame
        w_diff = 5.0  # Agora queremos ganhar peças
        w_mob = 1.0
        w_corner = 15.0
        w_pos = 1.0

    # 2. Mobilidade (Número de jogadas legais)
    # Precisamos simular a troca de turnos para calcular a mobilidade
    # Isso é custoso computacionalmente, mas vale a pena.
    original_player = state.player

    state.player = jogador
    mob_jogador = len(state.legal_moves())

    state.player = adversario
    mob_adversario = len(state.legal_moves())

    state.player = original_player  # Restaura estado original

    mobilidade = mob_jogador - mob_adversario

    # 3. Cantos e Posicionamento
    valor_cantos = 0
    valor_posicional = 0

    cantos_coords = [(0, 0), (0, 7), (7, 0), (7, 7)]

    # Cálculo rápido de cantos
    for cy, cx in cantos_coords:
        peca = tabuleiro[cy][cx]
        if peca == jogador:
            valor_cantos += 1
        elif peca == adversario:
            valor_cantos -= 1

    # Cálculo posicional (Weighted Matrix)
    for y in range(8):
        for x in range(8):
            peso = EVAL_TEMPLATE[y][x]
            peca = tabuleiro[y][x]
            if peca == jogador:
                valor_posicional += peso
            elif peca == adversario:
                valor_posicional -= peso

    # Somatório final ponderado
    score = (w_diff * diferenca_pecas) + \
            (w_mob * mobilidade) + \
            (w_corner * valor_cantos * 25) + \
            (w_pos * valor_posicional)

    return score