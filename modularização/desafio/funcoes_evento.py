def calcular_valor_base(tipo_ingresso, valor_padrao = 120):
    if tipo_ingresso in ["vip", "regular", "estudante"]:
        if tipo_ingresso == "vip":
            valor_base = valor_padrao * 1.5
        elif tipo_ingresso == "estudante":
            valor_base = valor_padrao * 0.6
        else:
            valor_base = valor_padrao
        print(f"Valor base do ingresso: R${valor_base:.2F}")
        return valor_base
    else:
        print("Dados Inválidos")


def calcular_extras(valor_base, oficinas = 0, material_extra = False):
    valor_oficinas = oficinas * 30
    if material_extra == True:
        valor_material_extra = 20
    else:
        valor_material_extra = 0
    valor_total = valor_base + valor_oficinas + valor_material_extra
    print(f"Valor total das oficinas: R${valor_oficinas:.2F} \nValor do material extra: R$R${valor_total:.2F}")
    return valor_total


def aplicar_desconto(valor_total, cupom = 0, taxa = 5):
    valor_desconto = valor_total * (cupom / 100)
    valor_total -= valor_desconto
    valor_taxa = valor_total * (taxa / 100)
    print(f"Valor do desconto: R${valor_desconto:.2F} \nValor da taxa: {valor_taxa:.2F} \nValor final a pagar: R${valor_total:.2F}")
    return valor_total


def classificar_inscricao(oficinas, material_extra):
    if oficinas >= 2 and material_extra == True:
        print("Inscrição completa")
    elif oficinas > 0:
        print("Inscrição Intermediária")
    else:
        print("Inscrição básica")


def gerear_relatorio_participante(tipo_ingresso, valor_padrao, oficinas, material_extra, cupom, taxa):
    print("")
    valor_base = calcular_valor_base(tipo_ingresso, valor_padrao)
    valor_total = calcular_extras(valor_base, oficinas, material_extra)
    valor_total = aplicar_desconto(valor_total, cupom, taxa)
    classificar_inscricao(oficinas, material_extra)