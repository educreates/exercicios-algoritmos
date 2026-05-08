# Exercício Integrador 3 — Relatório Semanal de Treino

---

Uma academia quer montar um pequeno sistema para registrar o resumo semanal de um aluno. O objetivo é calcular calorias, consolidar o tempo de treino e verificar se a meta foi atingida.

Neste exercício, você deverá construir um pequeno projeto com dois arquivos Python:

- `funcoes_treino.py` — contendo as funções;
- `principal_treino.py` — contendo a lógica principal do programa.

---

## Funções — `funcoes_treino.py`

### 1. `calcular_calorias(calorias_base, bonus=0)`

Crie uma função que receba a quantidade base de calorias gastas em um treino e um bônus opcional referente a uma atividade complementar. A função deve retornar o total de calorias.

**Exemplo:**

```
Entrada: calorias_base = 280, bonus = 40
Saída esperada: 320
```

---

### 2. `calcular_tempo_treino(tempo_principal, aquecimento=10)`

Crie uma função que receba o tempo principal do treino e um tempo opcional de aquecimento. A função deve retornar o tempo total do treino, em minutos.

**Exemplo:**

```
Entrada: tempo_principal = 45, aquecimento = 15
Saída esperada: 60
```

---

### 3. `analisar_desempenho(total_minutos)`

Crie uma função que receba o total de minutos treinados na semana. A função deve retornar dois valores: quantidade de horas completas e minutos restantes.

**Exemplo:**

```
Entrada: total_minutos = 135
Saída esperada: (2, 15)
```

---

### 4. `consolidar_treino(calorias, tempo, meta=300)`

Crie uma função que receba as calorias gastas, o tempo total treinado e uma meta opcional de calorias. A função deve retornar três valores: diferença para a meta, valor booleano indicando se a meta foi atingida e uma mensagem de resumo.

**Exemplo:**

```
Entrada: calorias = 320, tempo = 60, meta = 300
Saída esperada: (20, True, "Meta atingida")
```

---

## Lógica Principal — `principal_treino.py`

No arquivo principal, importe as funções do módulo e implemente a lógica do relatório.

O programa deve:

1. Ler a quantidade base de calorias do treino;
2. Ler o bônus opcional de calorias;
3. Calcular o total gasto;
4. Ler o tempo principal do treino;
5. Ler o tempo de aquecimento ou usar o valor padrão;
6. Calcular o tempo total;
7. Analisar o total de minutos e converter em horas e minutos;
8. Ler a meta semanal ou usar a meta padrão;
9. Consolidar os dados;
10. Exibir um relatório final.

---

## Saídas Esperadas

| Saída | Descrição |
|---|---|
| Calorias totais | Calorias base + bônus |
| Tempo total do treino | Tempo principal + aquecimento |
| Tempo em horas e minutos | Total de minutos convertido |
| Diferença para a meta | Calorias gastas menos a meta |
| Meta atingida | Booleano indicando o resultado |
| Mensagem de resumo | Texto final sobre o desempenho |

---

> **Observação:** neste integrador, o objetivo é mostrar como funções menores, organizadas em um arquivo separado, tornam mais simples a construção de um relatório maior e mais completo.