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

## Mini-Torneio das Heurísticas (Othello)

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
- Heurística mais vitoriosa: customizada 
- Total de vitórias: 3  
- Critério de desempate (peças capturadas): 154

---

# Detalhes da Implementação do Agente de Torneio

A arquitetura do agente foi projetada para resolver o compromisso entre a profundidade de busca e o limite de tempo. A implementação integra algoritmos de busca clássicos com heurísticas de gerenciamento de recursos.


## 1. Algoritmo de Busca: Minimax com Poda Alfa-Beta

A base da tomada de decisão é o algoritmo **Minimax**, implementado com a otimização de **Poda Alfa-Beta** (`minimax_move`).

**Justificativa:**  
O Minimax permite antecipar as respostas ótimas do adversário, enquanto a poda Alfa-Beta reduz drasticamente o número de nós visitados na árvore de jogo, cortando ramos que não influenciam a decisão final (quando `alfa >= beta` na maximização ou `beta <= alfa` na minimização). Isso permite alcançar profundidades maiores do que uma busca exaustiva simples.


## 2. Estratégia de Controle de Tempo: Aprofundamento Iterativo (Iterative Deepening)

Para garantir que o agente nunca exceda o tempo limite (o que causaria desclassificação imediata), não foi utilizada uma profundidade fixa. Em vez disso, implementou-se o **Aprofundamento Iterativo** no arquivo `tournament_agent.py`.

**Funcionamento:**  
O algoritmo realiza buscas sucessivas com profundidades crescentes (`d = 1, 2, 3, ...`).  
O resultado de cada iteração é salvo como a **melhor jogada provisória**.

**Predição de Custo:**  
Antes de iniciar uma nova profundidade, o agente estima o tempo necessário baseando-se no tempo gasto na iteração anterior multiplicado por um fator de ramificação (branching factor) estimado.  
Se a estimativa exceder o tempo restante (com margem de segurança de **0.2s**), o laço é interrompido e a melhor jogada da iteração anterior é retornada.


## 3. Função de Avaliação Híbrida

A função `evaluate_tournament` consolida lógicas presentes nos testes anteriores para criar uma avaliação robusta:

- Integra a análise posicional estática via **matriz de pesos**. Essa ideia veio da heuristica já previamente implementada no trabalho.  
- Calcula a **mobilidade relativa** (diferença de movimentos legais) e o **controle de cantos**. Essa parte do nosso código foi sugerida pelo modelo de IA Gemini, e implementada a partir da adaptação de uma função produzida pelo modelo. 
- Utiliza a **contagem de peças** (diferença absoluta) apenas nas fases finais do jogo, onde essa métrica define a vitória. Isso também é uma adaptação de uma heurística aplicada anteriorment.


## 4. Robustez e Otimizações

### Tratamento de Jogada Única
Foi adicionada uma verificação inicial que detecta se há apenas uma jogada legal disponível.  
Nesse caso, a busca é ignorada e a jogada é retornada imediatamente, economizando tempo de CPU.

---
# Heurística Customizada do Othello

A heurística implementada para avaliação dos estados do jogo Othello combina quatro fatores clássicos utilizados em Inteligência Artificial para jogos de tabuleiro: **diferença de peças**, **mobilidade**, **controle dos cantos** e **valor posicional**. O objetivo é produzir um valor numérico que indique quão favorável é o estado para o jogador sendo avaliado.

---

## Componentes da Heurística

### 1. Diferença de Peças (Piece Difference)

Conta quantas peças pertencem ao jogador e quantas pertencem ao adversário:

- Fórmula:  
  `diferença = peças_do_jogador – peças_do_adversário`

Esse fator representa vantagem material, mas recebe peso reduzido, já que possuir muitas peças cedo pode ser desvantajoso.

**Peso:** `1.0`

---

### 2. Mobilidade

Calcula quantos movimentos legais cada jogador possui:

- Fórmula:  
  `mobilidade = movimentos_do_jogador – movimentos_do_adversário`

Mobilidade reflete controle estratégico do tabuleiro e capacidade de evitar posições desfavoráveis.

**Peso:** `2.0`

---

### 3. Controle dos Cantos

Cantos são posições extremamente seguras: uma vez ocupados, nunca podem ser revertidos pelo adversário.

- Cada canto ocupado pelo jogador adiciona pontos.
- Cada canto ocupado pelo adversário subtrai pontos.

**Valor por canto:** `±25`  
**Peso final:** `3.0`

---

### 4. Valor Posicional (Positional Weights)

A heurística utiliza uma matriz 8×8 (EVAL_TEMPLATE) com pesos estratégicos para cada casa do tabuleiro:

- Cantos têm valores altos.  
- Casas vulneráveis próximas aos cantos têm valores negativos.  
- Bordas possuem valores positivos.  
- Centro possui valores moderados.

Essa tabela segue padrões clássicos encontrados em heurísticas amplamente utilizadas na literatura.

**Peso:** `0.5`

---

