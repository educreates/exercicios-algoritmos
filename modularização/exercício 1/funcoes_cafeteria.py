def calcular_preco_cafe(preco_base, acrescimo = 0):
    preco_cafe = preco_base + acrescimo
    print(f"O preço do café foi de {preco_cafe}")
    return preco_cafe


def calcular_acompanhamento(preco_acompanhamento, desconto = 0):
    preco_acompanhamento = preco_acompanhamento * (1 - (desconto / 100))
    return preco_acompanhamento


def resumo_item(nome, valor):
    print(f"nome: {nome}, valor: R${valor:.2F}")
    return nome, valor


def calcular_totais(valor1, valor2, valor3, taxa_de_servico = 0):
    valor_total = valor1 + valor2 + valor3
    taxa_de_servico = taxa_de_servico * (taxa_de_servico / 100)
    valor_total2 = valor_total + taxa_de_servico
    print(f"valor total: {valor_total}, taxa: {taxa_de_servico}, valor com taxa:{valor_total2}")
    return valor_total2