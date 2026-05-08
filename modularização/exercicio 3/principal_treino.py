import funcoes_treino as ft


calorias_base = int(input("Digite a quantidade de calorias perdidas no treino: "))
bonus = int(input("Digite o bonûs de calorias perdidas no cardio: "))


total_calorias = ft.calcular_calorias(calorias_base, bonus)


minutos = int(input("Digite o tempo (em minutos) gasto para realizar o treino: "))
aquecimento = int(input("Digite o tempo gasto com o aquecimento: "))


tempo_total = ft.calcular_tempo_treino(minutos, aquecimento)


ft.analisar_desempenho(tempo_total)


meta = int(input("Digite a meta diária de perda de calorias: "))


ft.consolidar_treino(total_calorias, tempo_total, meta)