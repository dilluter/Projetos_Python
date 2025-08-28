ano = int(input("Digite um ano entre 1970 e 2025: "))

if 1970 <= ano <= 2025:
    if (ano - 1930) % 4 == 0:
        print(f"{ano} foi um ano de Copa do Mundo!")
    else:
        print(f"{ano} não foi um ano de Copa do Mundo.")
else:
    print("Ano fora do intervalo permitido.")
