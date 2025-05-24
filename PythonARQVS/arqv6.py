# Solicita a idade do usuário
idade = int(input("Digite a sua idade: "))

# Classifica a pessoa com base na idade
if idade < 0:
    print("Idade inválida.")
elif idade <= 12:
    print("Você é uma criança.")
elif idade <= 17:
    print("Você é um adolescente.")
elif idade <= 64:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")