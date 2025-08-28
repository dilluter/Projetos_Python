import random

print("Gerando 10 números aleatórios e verificando se são pares ou ímpares:\n")

for i in range(10):
    numero = random.randint(1, 100)
    if numero % 2 == 0:
        print(f"{i+1}. O número {numero} é PAR.")
    else:
        print(f"{i+1}. O número {numero} é ÍMPAR.")
