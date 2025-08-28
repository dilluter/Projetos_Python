segundos = int(input("Digite a duração em segundos: "))

horas = int(segundos / 3600)
resto = int(segundos % 3600)
minutos = int (resto / 60)
segundos_restantes = int(resto % 60)

print(f"{horas}h:{minutos:02d}min:{segundos_restantes}s")

