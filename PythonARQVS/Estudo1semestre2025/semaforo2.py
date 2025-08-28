cor = input("Digite uma cor (verde, amarelo ou vermelho): ").lower()

if cor == "verde":
    print("SIGA.")
elif cor == "vermelho":
    print("PARE.")
elif cor == "amarelo":
    print("ATENÇÃO.")
else:
    print("Cor inválida.")
