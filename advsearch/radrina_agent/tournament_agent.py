import time
from typing import Tuple
from ..othello.gamestate import GameState
from .minimax import minimax_move

EVAL_TEMPLATE = [
    [100, -30, 6, 2, 2, 6, -30, 100],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [  6,   1, 1, 1, 1, 1,   1,   6],
    [  2,   1, 1, 3, 3, 1,   1,   2],
    [  2,   1, 1, 3, 3, 1,   1,   2],
    [  6,   1, 1, 1, 1, 1,   1,   6],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [100, -30, 6, 2, 2, 6, -30, 100],
]


def make_move(state: GameState) -> Tuple[int, int]:

    inicio = time.perf_counter()
    LIMITE = 5.0

    melhor_jogada = None
    profundidade = 1

    # Aprofundamento iterativo
    while True:
        if time.perf_counter() - inicio >= LIMITE:
            break

        jogada = minimax_move(state, max_depth = profundidade, eval_func = evaluate_tournament)

        if jogada is not None:
            melhor_jogada = jogada

        profundidade += 1

        if profundidade > 12:
            break

    return melhor_jogada


def evaluate_tournament(state, jogador: str) -> float:

    tabuleiro = state.board.tiles
    adversario = 'W' if jogador == 'B' else 'B'

    # -------------------------------
    # Diferença bruta de peças
    # -------------------------------
    pecas_jog = sum(linha.count(jogador) for linha in tabuleiro)
    pecas_adv = sum(linha.count(adversario) for linha in tabuleiro)
    diff_pecas = pecas_jog - pecas_adv

    # -------------------------------
    # Mobilidade
    # -------------------------------
    jog_original = state.player

    state.player = jogador
    mov_jog = len(state.get_actions())

    state.player = adversario
    mov_adv = len(state.get_actions())

    state.player = jog_original

    mobilidade = mov_jog - mov_adv

    # -------------------------------
    # Controle dos cantos
    # -------------------------------
    cantos = [(0,0),(0,7),(7,0),(7,7)]
    score_cantos = 0

    for y, x in cantos:
        if tabuleiro[y][x] == jogador:
            score_cantos += 50
        elif tabuleiro[y][x] == adversario:
            score_cantos -= 50

    # -------------------------------
    # Estabilidade aproximada
    # (semelhante a heurísticas de artigos clássicos)
    # -------------------------------
    estabilidade = 0
    borda = {0, 7}

    for y in range(8):
        for x in range(8):
            if tabuleiro[y][x] == jogador:
                if y in borda or x in borda:
                    estabilidade += 5
            elif tabuleiro[y][x] == adversario:
                if y in borda or x in borda:
                    estabilidade -= 5

    # -------------------------------
    # Frontier discs (peças vulneráveis)
    # -------------------------------
    frontier_penalty = 0
    direcoes = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

    for y in range(8):
        for x in range(8):
            if tabuleiro[y][x] == jogador:
                for dx, dy in direcoes:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < 8 and 0 <= nx < 8 and tabuleiro[ny][nx] == '.':
                        frontier_penalty -= 3
                        break
            elif tabuleiro[y][x] == adversario:
                for dx, dy in direcoes:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < 8 and 0 <= nx < 8 and tabuleiro[ny][nx] == '.':
                        frontier_penalty += 3
                        break

    # -------------------------------
    # Máscara posicional
    # -------------------------------
    score_mask = 0
    for y in range(8):
        for x in range(8):
            peso = EVAL_TEMPLATE[y][x]
            if tabuleiro[y][x] == jogador:
                score_mask += peso
            elif tabuleiro[y][x] == adversario:
                score_mask -= peso

    # -------------------------------
    # Combinação ponderada
    # -------------------------------
    return (
        0.3 * diff_pecas +
        2.5 * mobilidade +
        3.5 * score_cantos +
        1.8 * estabilidade +
        1.0 * score_mask +
        1.2 * frontier_penalty
    )