n1 = float(input("DIGITE O PRIMEIRO NÚMERO: "))
n2 = float(input("DIGITE O SEGUNDO NÚMERO: "))
n3 = float(input("DIGITE O TERCEIRO NÚMERO: "))
n4 = float(3)

media = (n1 + n2 + n3) / n4

if all(0 <= n <= 100 for n in [n1, n2, n3]):
    print(f"A média aritmética entre os números {n1}, {n2}, e {n3} é {media}.")
else:
    print("ERRO: Todos os números devem estar entre (0 a 100).")
