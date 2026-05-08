def calcular_passagem(preco_base, bagagem = 0):
    valor_passagem = preco_base + bagagem
    print(f"Valor final da passagem: {valor_passagem:.2F}")
    return valor_passagem


def calcular_hospedagem(taxa_extra, valor_diaria, dias = 1):
    valor_hospedagem = (valor_diaria * dias) + taxa_extra
    print(f"Valor final da hospedagem: R${valor_hospedagem:.2F}")
    return valor_hospedagem


def converter_duracao(total_horas):
    horas_restantes = total_horas % 24
    dias_completos = (total_horas - horas_restantes) / 24
    print(f"Dias completos na viagem: {dias_completos}, horas restantes: {horas_restantes}")
    return dias_completos, horas_restantes


def calcular_orcamento(valor_passagem, valor_hospedagem, alimentacao):
    custo_fixo = valor_hospedagem + valor_passagem
    custo_extra = alimentacao
    custo_total = custo_fixo + custo_extra
    print(f"custo fixo: R${custo_fixo:.2F}, custo extra: R${custo_extra:.2F}, custo total geral: R${custo_total:.2F}")
    return custo_total, custo_extra, custo_fixo