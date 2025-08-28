def funcao():
    condicao = True  
    if condicao:
        raise Exception("Descrição do erro")


try:
    funcao()
except Exception as e:
    print(f"Erro: {str(e)}")