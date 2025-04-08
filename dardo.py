a = int(input("digite o primeiro valor: "))
b = int(input("digite o segundo valor: "))
c = int(input("digite o terceiro valor: "))

if a <= b and a <= c:
    print(f"O menor valor é: {a}")
elif b <= a and b <= c:
    print(f"O menor valor é: {b}")
else:
    print(f"O menor valor é: {c}")