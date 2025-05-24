premios = [15, 85, 86]

for i in range(1, 4):
    try:
        n1 = float(input(f"Tentativa {i} - Digite um número entre 0 e 100: "))
    except ValueError:
        print("Digite um número válido.")
        continue

    acertou = False
    for premio in premios:
        if n1 == premio:
            acertou = True
            print("Parabéns! Você acertou!")
            break

    if acertou:
        break
