idade = int(input("Digite sua idade: "))
tem_carteira = input("Você tem carteira de motorista? (s/n): ").lower()

if idade >= 18 and tem_carteira == 's':
    print("Você pode dirigir.")
else:
    print("Você NÃO pode dirigir.")
