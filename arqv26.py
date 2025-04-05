try:
    # Código que pode gerar uma exceção
    with open("arquivo.txt", "r") as arquivo:
        # Realizar operações com o arquivo
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")