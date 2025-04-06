nome = input("Digite o nome do funcionário: ")
valor_hora = float(input("Digite o valor que o funcionário recebe por hora: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))

salario = valor_hora * horas_trabalhadas

print(f"O funcionário {nome} receberá R$ {salario:.2f}")
