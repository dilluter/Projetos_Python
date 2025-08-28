print("=== Cardápio da Lanchonete ===")
print("1 - X-Burguer      R$ 10.00")
print("2 - X-Salada       R$ 12.00")
print("3 - Refrigerante   R$ 5.00")
print("4 - Suco           R$ 6.00")
print("5 - Batata Frita   R$ 8.00")
print("0 - Finalizar pedido")

total = 0

while True:
    codigo = int(input("Digite o código do produto (0 para sair): "))

    if codigo == 0:
        break

    quantidade = int(input("Digite a quantidade desejada: "))

    if codigo == 1:
        preco = 10.00
    elif codigo == 2:
        preco = 12.00
    elif codigo == 3:
        preco = 5.00
    elif codigo == 4:
        preco = 6.00
    elif codigo == 5:
        preco = 8.00
    else:
        print("Código inválido!")
        continue  # volta para o início do loop

    subtotal = preco * quantidade
    total += subtotal
    print(f"Subtotal do item: R$ {subtotal:.2f}")
    print(f"Total parcial: R$ {total:.2f}\n")

print(f"\nPedido finalizado! Total a pagar: R$ {total:.2f}")
