valor_produto = float(input("Digite o valor do produto: R$ "))
valor_pago = float(input("Digite o valor pago pelo cliente: R$ "))

if valor_pago < valor_produto:
    print("Valor insuficiente. O cliente precisa pagar mais.")
else:
    troco = valor_pago - valor_produto
    print(f"Troco a ser devolvido: R$ {troco:.2f}")
