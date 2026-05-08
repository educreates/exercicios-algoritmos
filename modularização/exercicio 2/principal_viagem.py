import funcoes_viagem as fv


valor_base = float(input("Digite o valor base da passagem: "))
taxa_bagagem = float(input("Digite a taxa opcional de bagagem: "))


valor_passagem = fv.calcular_passagem(valor_base, taxa_bagagem)


diaria = float(input("Digite o valor da diária do hotel: "))
dias = int(input("Digite quantos dias de hospedagem serão comprados: "))
taxa_hospedagem = float(input("Digite a taxa opcional de hospedagem: "))


valor_hospedagem = fv.calcular_hospedagem(taxa_hospedagem, diaria, dias)


horas = int(input("Digite o tempo de duração total da viagem em horas: "))


fv.converter_duracao(horas)


alimentacao = float(input("Digite o gasto opcional com alimentação: "))


fv.calcular_orcamento(valor_passagem, valor_hospedagem, alimentacao)