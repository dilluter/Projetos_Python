n1 = float(30)
n2 = float(20)
n3 = float(10)
n4 = float(3)

media = (n1 + n2 + n3) / n4

if all(0 <= n <= 100 for n in [n1, n2, n3]):
    print(f"A média aritmética entre os números {n1}, {n2}, e {n3} é {media}.")
else:
    print("ERRO: Todos os números devem estar entre (0 a 100).")
