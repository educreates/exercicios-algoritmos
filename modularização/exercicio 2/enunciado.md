# Exercício Integrador 2 — Planejamento Básico de Viagem

---

Uma pessoa deseja fazer uma viagem curta e quer usar um programa simples para estimar os custos principais e organizar melhor as informações.

Neste exercício, você deverá construir um pequeno projeto com dois arquivos Python:

- `funcoes_viagem.py` — contendo as funções;
- `principal_viagem.py` — contendo a lógica principal do programa.

---

## Funções — `funcoes_viagem.py`

### 1. `calcular_passagem(valor_base, bagagem=0)`

Crie uma função que receba o valor base da passagem e uma taxa opcional de bagagem. A função deve retornar o valor final da passagem.

**Exemplo:**

```
Entrada: valor_base = 350.0, bagagem = 80.0
Saída esperada: 430.0
```

---

### 2. `calcular_hospedagem(valor_diaria, dias=1, taxa_extra=0)`

Crie uma função que receba o valor da diária, a quantidade de dias e uma taxa extra opcional. A função deve retornar o valor final da hospedagem.

**Exemplo:**

```
Entrada: valor_diaria = 200.0, dias = 3, taxa_extra = 50.0
Saída esperada: 650.0
```

---

### 3. `converter_duracao(total_horas)`

Crie uma função que receba a duração total de uma viagem em horas. A função deve retornar dois valores: a quantidade de dias completos e a quantidade de horas restantes.

**Exemplo:**

```
Entrada: total_horas = 53
Saída esperada: (2, 5)
```

---

### 4. `calcular_orcamento(passagem, hospedagem, alimentacao=0)`

Crie uma função que receba o valor da passagem, o valor da hospedagem e um gasto opcional com alimentação. A função deve retornar três valores: custo fixo, custo extra e custo total geral.

**Exemplo:**

```
Entrada: passagem = 430.0, hospedagem = 650.0, alimentacao = 120.0
Saída esperada: (1080.0, 120.0, 1200.0)
```

---

## Lógica Principal — `principal_viagem.py`

No arquivo principal, importe as funções criadas e desenvolva a lógica da aplicação.

O programa deve:

1. Ler o valor base da passagem;
2. Ler a taxa opcional de bagagem;
3. Calcular o valor final da passagem;
4. Ler o valor da diária;
5. Ler a quantidade de dias;
6. Ler uma taxa extra opcional da hospedagem;
7. Calcular o valor final da hospedagem;
8. Ler a duração total da viagem em horas;
9. Converter essa duração em dias e horas;
10. Ler o gasto opcional com alimentação;
11. Calcular o orçamento geral;
12. Exibir um resumo final da viagem.

---

## Saídas Esperadas

| Saída | Descrição |
|---|---|
| Valor final da passagem | Valor base + taxa de bagagem |
| Valor final da hospedagem | Diária × dias + taxa extra |
| Duração convertida | Total de horas expresso em dias e horas |
| Custo fixo | Passagem + hospedagem |
| Custo extra | Gastos com alimentação |
| Custo total da viagem | Custo fixo + custo extra |

---

> **Observação:** este exercício foi planejado para mostrar como o uso de parâmetros opcionais permite flexibilizar cálculos e como o retorno múltiplo ajuda a organizar melhor a saída de uma aplicação maior.