def calcular_valor(horario, distancia):
    hora, minuto = map(int, horario.split(":"))
    minutos_totais = hora * 60 + minuto

    if 0 <= minutos_totais <= 360:  # 0:00 às 6:00
        valor_fixo = 5.30
        valor_por_km = 4.40
    elif 361 <= minutos_totais <= 1080:  # 6:01 às 18:00
        valor_fixo = 3.30
        valor_por_km = 3.80
    else:  # 18:01 às 23:59
        valor_fixo = 4.30
        valor_por_km = 4.10

    return round(valor_fixo + (valor_por_km * distancia), 2)

# Exemplo com entrada do usuário
horario = input("Digite o horário (HH:MM): ")
distancia = float(input("Digite a distância percorrida (em km): "))
valor = calcular_valor(horario, distancia)
print(f"Valor a pagar: R$ {valor:.2f}")
