import funcoes_evento as fe

tipo_ingresso = input("Digite o tipo do ingresso levando em conta as opções a seguir \n'vip' \n'regular' \n'estudante' \n")
valor_padrao = float(input("Digite o valor padrão do preço do ingresso \n"))
oficinas = int(input("Digite a quantidade de oficinas \n"))
material_extra = bool(input("Digite se foi usado material extra \nUse 'True' ou 'False' \n"))
cupom = int(input("Digite o valor do desconto do cupom \n"))
taxa = int(input("Digite o valor do desconto da taxa \n"))

fe.gerear_relatorio_participante(tipo_ingresso, valor_padrao, oficinas, material_extra, cupom, taxa)