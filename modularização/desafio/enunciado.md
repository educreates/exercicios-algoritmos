# 🏆 DESAFIO — Sistema de Relatório Completo de Inscrições em Evento

---

Uma organização está desenvolvendo um sistema para consolidar inscrições em um evento temático com oficinas e atividades extras. Diferentemente dos exercícios anteriores, este desafio exige uma solução mais robusta, com funções mais elaboradas, encadeamento de chamadas e maior decomposição do problema.

O objetivo é construir uma pequena aplicação organizada em módulos, em que cada função fique responsável por uma etapa do processamento, e algumas delas dependam diretamente do resultado de outras.

---

## Estrutura Esperada do Projeto

Você deverá criar dois arquivos Python:

- `funcoes_evento.py` — com as funções auxiliares e de processamento;
- `principal_evento.py` — com a lógica principal do programa.

---

## Funções — `funcoes_evento.py`

### 1. `calcular_valor_base(tipo_ingresso, valor_padrao=120)`

Crie uma função que receba o tipo de ingresso escolhido pelo participante e um valor padrão opcional. Considere os seguintes multiplicadores sobre o valor padrão:

- `"regular"` → 100% do valor padrão;
- `"vip"` → 150% do valor padrão;
- `"estudante"` → 60% do valor padrão.

A função deve retornar o valor base calculado para o ingresso.

**Exemplo:**

```
Entrada: tipo_ingresso = "vip", valor_padrao = 120
Saída esperada: 180.0
```

---

### 2. `calcular_extras(valor_base, oficinas=0, material_extra=False)`

Crie uma função que receba o valor base do ingresso, a quantidade de oficinas extras escolhidas e uma indicação booleana informando se o participante deseja material extra.

Considere as seguintes regras:

- cada oficina extra adiciona R$ 30,00;
- se houver material extra, adicionar R$ 20,00.

A função deve retornar três valores: valor total das oficinas, valor do material extra e valor parcial atualizado.

**Exemplo:**

```
Entrada: valor_base = 120.0, oficinas = 2, material_extra = True
Saída esperada: (60.0, 20.0, 200.0)
```

---

### 3. `aplicar_desconto(valor_parcial, cupom=0, taxa_admin=5)`

Crie uma função que receba um valor parcial, um desconto percentual opcional de cupom e uma taxa administrativa percentual padrão.

A função deve:

- calcular o valor do desconto;
- aplicar o desconto;
- calcular a taxa administrativa sobre o valor já descontado;
- retornar três valores: valor do desconto, valor da taxa administrativa e valor final a pagar.

**Exemplo:**

```
Entrada: valor_parcial = 200.0, cupom = 10, taxa_admin = 5
Saída esperada: (20.0, 9.0, 189.0)
```

---

### 4. `classificar_participacao(oficinas, material_extra, total_final)`

Crie uma função que receba a quantidade de oficinas, a informação sobre material extra e o valor final da inscrição. A função deve retornar uma classificação textual para o perfil da inscrição.

Regras de classificação:

- 2 ou mais oficinas **e** material extra → `"Inscrição completa"`;
- pelo menos 1 oficina → `"Inscrição intermediária"`;
- caso contrário → `"Inscrição básica"`.

**Exemplo:**

```
Entrada: oficinas = 2, material_extra = True, total_final = 189.0
Saída esperada: "Inscrição completa"
```

---

### 5. `gerar_relatorio_participante(nome, tipo_ingresso, valor_padrao, oficinas, material_extra, cupom=0)`

> ⚠️ **Função principal do desafio** — esta função encadeia todas as anteriores.

Ela deve:

1. chamar `calcular_valor_base`;
2. usar o resultado para chamar `calcular_extras`;
3. usar o valor parcial para chamar `aplicar_desconto`;
4. usar o total final para chamar `classificar_participacao`;
5. retornar múltiplos valores com os principais dados consolidados do participante.

A função deve retornar:

- valor base;
- valor das oficinas;
- valor do material;
- valor do desconto;
- valor da taxa administrativa;
- valor final;
- classificação da inscrição.

**Exemplo:**

```
Entrada: nome = "Marina", tipo_ingresso = "vip", valor_padrao = 120,
         oficinas = 2, material_extra = True, cupom = 10
Saída esperada: (180.0, 60.0, 20.0, 26.0, 11.7, 245.7, "Inscrição completa")
```

---

## Lógica Principal — `principal_evento.py`

No arquivo principal, importe as funções do módulo e desenvolva a lógica do sistema.

O programa deve processar os dados de **3 participantes**. Para cada participante, o programa deve:

1. Ler o nome;
2. Ler o tipo de ingresso;
3. Ler a quantidade de oficinas extras;
4. Ler se deseja material extra;
5. Ler um cupom de desconto opcional;
6. Chamar a função `gerar_relatorio_participante`;
7. Exibir um resumo organizado daquele participante.

---

## Saídas Esperadas

| Saída | Descrição |
|---|---|
| Nome do participante | Texto livre |
| Tipo de ingresso | regular, vip ou estudante |
| Valor base do ingresso | Calculado conforme o tipo |
| Valor total das oficinas extras | Quantidade × R$ 30,00 |
| Valor do material extra | R$ 20,00 se solicitado |
| Valor do desconto aplicado | Percentual do cupom |
| Valor da taxa administrativa | 5% sobre o valor descontado |
| Valor final da inscrição | Total a pagar |
| Classificação da inscrição | Básica, intermediária ou completa |

---

## ✅ Requisitos Adicionais do Desafio

- Organizar corretamente as funções no arquivo de biblioteca;
- Importar as funções no arquivo principal;
- Usar parâmetros opcionais em mais de uma função;
- Usar retornos múltiplos em mais de uma função;
- Construir pelo menos uma função com encadeamento de chamadas entre funções;
- Evitar repetir código no arquivo principal.

---

> **Observação:** diferentemente dos exercícios anteriores, este desafio exige maior planejamento e organização. O encadeamento de funções é o ponto central — domine-o e o restante se resolve naturalmente.