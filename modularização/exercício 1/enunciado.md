# Exercício Integrador 1 - Fechamento de pedido de uma cafeteria
 
---
 
Uma cafeteria deseja organizar melhor o fechamento dos pedidos. Para isso, o sistema deve calcular o valor do café, o valor do acompanhamento, gerar pequenos resumos dos itens e, ao final, calcular os totais do pedido.
 
Neste exercício, você deverá construir um pequeno projeto com dois arquivos Python:
 
- `funcoes_cafeteria.py` — contendo as funções;
- `principal_cafeteria.py` — contendo a lógica principal do programa.

---
 
## Funções — `funcoes_cafeteria.py`
 
### 1. `calcular_preco_cafe(preco_base, acrescimo=0)`
 
Crie uma função que receba o preço base de um café e um acréscimo opcional referente ao tamanho escolhido. A função deve retornar o preço final da bebida.
 
**Exemplo:**
 
```
Entrada: preco_base = 8.0, acrescimo = 2.0
Saída esperada: 10.0
```
 
---
 
### 2. `calcular_acompanhamento(preco, desconto=0)`
 
Crie uma função que receba o preço de um acompanhamento e um desconto percentual opcional. A função deve retornar o valor final do acompanhamento após aplicar o desconto informado.
 
**Exemplo:**
 
```
Entrada: preco = 12.0, desconto = 25
Saída esperada: 9.0
```
 
---
 
### 3. `resumo_item(nome, valor)`
 
Crie uma função que receba o nome de um item e seu valor final. A função deve retornar dois valores: uma string com a descrição do item e o valor formatado para exibição.
 
**Exemplo:**
 
```
Entrada: nome = "Capuccino", valor = 10.5
Saída esperada: ("Capuccino", "R$ 10.50")
```
 
---
 
### 4. `calcular_totais(valor1, valor2, taxa_servico=10)`
 
Crie uma função que receba os valores de dois itens e uma taxa de serviço opcional. A função deve retornar três valores: subtotal, valor da taxa e total final do pedido.
 
**Exemplo:**
 
```
Entrada: valor1 = 10.0, valor2 = 8.0, taxa_servico = 10
Saída esperada: (18.0, 1.8, 19.8)
```
 
---
 
## Lógica principal — `principal_cafeteria.py`
 
No arquivo principal, importe as funções criadas e desenvolva a lógica do sistema.
 
O programa deve:
 
1. Ler o nome e o preço base do café;
2. Ler o acréscimo opcional do tamanho;
3. Ler o nome e o preço do acompanhamento;
4. Ler o desconto opcional do acompanhamento;
5. Calcular os valores finais dos dois itens;
6. Gerar o resumo de cada item;
7. Calcular subtotal, taxa e total do pedido;
8. Exibir um resumo final do pedido.

---
 
## Entradas e saídas esperadas
 
**Entradas sugeridas:**
 
| Campo | Descrição |
|---|---|
| Nome do café | Texto livre |
| Preço base do café | Valor numérico |
| Acréscimo do tamanho | Valor numérico (opcional) |
| Nome do acompanhamento | Texto livre |
| Preço do acompanhamento | Valor numérico |
| Desconto do acompanhamento | Percentual (opcional) |
| Taxa de serviço | Percentual (opcional) |
 
**Saídas esperadas:**
 
| Saída | Descrição |
|---|---|
| Resumo do café | Nome e valor formatado |
| Resumo do acompanhamento | Nome e valor formatado |
| Subtotal | Soma dos dois itens |
| Taxa de serviço | Valor calculado sobre o subtotal |
| Total final | Subtotal + taxa |
 
---
 
> **Observação:** neste exercício, o objetivo é demonstrar como funções com *parâmetros opcionais* e *retornos múltiplos* podem ser organizadas em um módulo separado e reutilizadas em um programa principal.
