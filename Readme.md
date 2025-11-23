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

