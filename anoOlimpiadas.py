ano = int(input("Digite um ano entre 1890 e 2025: "))

if 1890 <= ano <= 2025:
    if (ano - 1896) % 4 == 0 and ano not in [1916, 1940, 1944]:
        print(f"{ano} foi um ano de Jogos Olímpicos!")
    else:
        print(f"{ano} não foi um ano de Jogos Olímpicos.")
else:
    print("Ano fora do intervalo permitido.")
