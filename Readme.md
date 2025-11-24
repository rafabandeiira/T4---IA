# Trabalho 4 – Busca com Adversário  

## Integrantes do Grupo

- **Carolina Magagnin Wajner – 134101 – Turma A**  
- **Rafael Silveira Bandeira – 584789 – Turma A**  
- **Rodrigo Salvadori Feldens – 578803 – Turma A**

--- 

## Bibliotecas Necessárias

O trabalho foi desenvolvido utilizando **Python 3.12**.

Além das bibliotecas já descritas no enunciado (instaladas no ambiente padrão disponibilizado:  
**numpy**, **pandas**, **numba**), **não utilizamos nenhuma dependência extra**.

Portanto, não há necessidade de instalação adicional de pacotes via `pip`.

Caso esteja executando o kit em outro ambiente, certifique-se apenas de ter:

- Python 3.12+
- numpy
- pandas
- numba

---

## Avaliação do Minimax no Tic-Tac-Toe Misere (Item 2.2.a)

Para o jogo da velha invertido, implementamos o algoritmo **minimax com poda alfa-beta** com profundidade ilimitada.  
A função de utilidade (`utility`) atribui valores positivos, negativos ou zero apenas para estados **terminais**, conforme especificado no enunciado.

Realizamos três tipos de avaliação, conforme solicitado:

### (i) O minimax sempre ganha ou empata contra o randomplayer?

Sim.  
Testes repetidos mostram que o nosso agente **nunca perde** para o `randomplayer`.  
Como o jogo é totalmente resolvido pela busca completa, o minimax sempre encontra:

- vitórias quando o oponente comete erros, e  
- empates quando o oponente joga “por acaso” mas cai em linhas neutras.

Esse comportamento também é confirmado pelo teste `test_proven_win_exploiting_first_blunder`, que garante que o agente identifica automaticamente uma linha vencedora quando o oponente faz uma jogada não-ótima.

### (ii) O minimax sempre empata consigo mesmo?

Sim.  
Quando nosso minimax joga contra ele mesmo, todas as partidas testadas terminam em **empate**, o que indica:

- jogo perfeito por ambas as partes,  
- ausência de jogadas subótimas,  
- simetria e consistência nas decisões.

Isso também é evidenciado pelo teste `test_perfect_play`, que verifica que o agente sempre escolhe as únicas jogadas ótimas em sequências conhecidas da solução perfeita do Tic-Tac-Toe Misere.

### (iii) O minimax perde contra um humano usando sua melhor estratégia?

Não.  
Tentamos explorar manualmente diferentes aberturas e sequências conhecidas, e o agente **nunca perde**.  
Assim como no item anterior, a profundidade total do jogo é pequena (máximo 9), então o minimax calcula o jogo completo e garante um resultado ótimo independentemente da estratégia do humano.

### **Conclusão**

A partir das evidências experimentais e dos testes automatizados:

- o agente nunca perde para jogadas aleatórias,
- empata consigo mesmo consistentemente,
- e não perde para jogadores humanos.

Portanto, concluímos que nossa implementação joga o Tic-Tac-Toe Misere de forma **perfeita ou virtualmente perfeita**, conforme esperado de um minimax completo com poda alfa-beta.

---

## Lista de Comandos para testar o Othello:

### 1. HUMANO vs SUAS 3 HEURÍSTICAS
- python server.py othello advsearch/humanplayer/agent.py advsearch/radrina_agent/othello_minimax_count.py
- python server.py othello advsearch/humanplayer/agent.py advsearch/radrina_agent/othello_minimax_mask.py
- python server.py othello advsearch/humanplayer/agent.py advsearch/radrina_agent/othello_minimax_custom.py

### 2. RANDOM vs SUAS 3 HEURÍSTICAS
- python server.py othello advsearch/randomplayer/agent.py advsearch/radrina_agent/othello_minimax_count.py
- python server.py othello advsearch/randomplayer/agent.py advsearch/radrina_agent/othello_minimax_mask.py
- python server.py othello advsearch/randomplayer/agent.py advsearch/radrina_agent/othello_minimax_custom.py

### 3. MINI-TORNEIO — TODAS AS PARTIDAS ENTRE AS 3 HEURÍSTICAS

- Contagem de peças X Valor posicional: python server.py othello advsearch/radrina_agent/othello_minimax_count.py advsearch/radrina_agent/othello_minimax_mask.py
- Valor posicional X Contagem de peças: python server.py othello advsearch/radrina_agent/othello_minimax_mask.py advsearch/radrina_agent/othello_minimax_count.py
- Contagem de peças X Heurística customizada: python server.py othello advsearch/radrina_agent/othello_minimax_count.py advsearch/radrina_agent/othello_minimax_custom.py
- Heurística customizada X Contagem de peças: python server.py othello advsearch/radrina_agent/othello_minimax_custom.py advsearch/radrina_agent/othello_minimax_count.py
- Valor posicional X Heurística customizada: python server.py othello advsearch/radrina_agent/othello_minimax_mask.py advsearch/radrina_agent/othello_minimax_custom.py
- Heurística customizada X Valor posicional: python server.py othello advsearch/radrina_agent/othello_minimax_custom.py advsearch/radrina_agent/othello_minimax_mask.py

### 4. HUMAN vs AGENTE DO TORNEIO
python server.py othello advsearch/humanplayer/agent.py advsearch/radrina_agent/tournament_agent.py

### 5. RANDOM vs AGENTE DO TORNEIO
python server.py othello advsearch/randomplayer/agent.py advsearch/radrina_agent/tournament_agent.py

---

# Mini-Torneio das Heurísticas (Othello)

A tabela abaixo resume as 6 partidas obrigatórias entre as três heurísticas:  
**Contagem de peças**, **Valor posicional** e **Heurística customizada**.

| Partida | Preto (começa)         | Branco                 | Vencedor               | Peças (P × B) |
|--------|------------------------|------------------------|------------------------|---------|
| 1 | Contagem de peças      | Valor posicional       | Contagem de peças      | 37 X 27 |
| 2 | Valor posicional       | Contagem de peças      | Contagem de peças      | 26 X 38 |
| 3 | Contagem de peças      | Heurística customizada | Heurística customizada | 19 X 45 |
| 4 | Heurística customizada | Contagem de peças      | Contagem de peças      | 20 X 44 |
| 5 | Valor posicional       | Heurística customizada | Heurística customizada | 20 X 44 |
| 6 | Heurística customizada | Valor posicional       | Heurística customizada | 45 X 19 |

---

## Resumo Final do Desempenho
- Heurística mais vitoriosa:  
- Total de vitórias:  
- Critério de desempate (peças capturadas):  