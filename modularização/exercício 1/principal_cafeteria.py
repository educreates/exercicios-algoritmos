import funcoes_cafeteria as fc


#nome = input("Digite o nome do café: ")
#preco_base = float(input("Digite o preço base do café: "))
#acrescimo = float(input("Digite o valor do acréscimo opcional: "))
#desconto = float(input("Digite o valor do desconto: "))

#valor1 = float(input("Digite o valor do item 1: "))
#valor2 = float(input("Digite o valor do item 2: "))
#acompanhamento = float(input("Digite o valor do acompanhamento"))


nome = input("Digite o nome do café: ")
preco_base1 = float(input("Digite o preço base do café: "))
acrescimo = float(input("Digite o valor do acréscimo opcional: "))
fc.calcular_preco_cafe(preco_base1, acrescimo)
fc.resumo_item(nome, preco_base1)


nome = input("Digite o nome do café: ")
preco_base2 = float(input("Digite o preço base do café: "))
acrescimo = float(input("Digite o valor do acréscimo opcional: "))
fc.calcular_preco_cafe(preco_base2, acrescimo)
fc.resumo_item(nome, preco_base2)


acompanhamento = float(input("Digite o valor do acompanhamento"))
desconto = float(input("Digite o valor do desconto: "))
fc.calcular_acompanhamento(acompanhamento, desconto)


taxa_de_servico = int(input("Digite o valor da taxa de serviço"))
fc.calcular_totais(preco_base1, preco_base2, acompanhamento, taxa_de_servico)