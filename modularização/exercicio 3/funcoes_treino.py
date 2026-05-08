def calcular_calorias(calorias_base, bonus = 0):
    total_calorias = calorias_base + bonus
    print(f"O total de calorias gastas durante o treino foi igual a {total_calorias}")
    return total_calorias


def calcular_tempo_treino(tempo_principal, aquecimento = 10):
    tempo_total = tempo_principal + aquecimento
    print(f"O tempo total de treino foi de {tempo_total} minutos")
    return tempo_total


def analisar_desempenho(tempo_total):
    tempo_semanal = tempo_total * 5
    minutos_restantes = tempo_semanal % 60
    horas_semanais = (tempo_semanal - minutos_restantes) / 60
    print(f"Foram gastos {horas_semanais} horas e {minutos_restantes} minutos em treinos durante a semana.")


def consolidar_treino(total_calorias, tempo_total, meta = 300):
    diferenca = total_calorias - meta
    if diferenca < 0:
        meta = False
        print(f"A diferença para de calorias perdidas para a meta é de {diferenca}, {bool(meta)}, Meta não atingida")
    else:
        print(f"A diferença para de calorias perdidas para a meta é de {diferenca}, {bool(meta)}, Meta atingida")