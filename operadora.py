minutos = int(input("DIGITE A QUANTIDADE DE MINUTOS "))
valor_pago = 50 
if minutos > 100:
    valor_pago += 2 * (minutos - 100)
    print(f"valor a pagar : ${valor_pago}")
           

