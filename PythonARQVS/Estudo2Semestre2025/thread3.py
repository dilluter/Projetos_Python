import time
import threading
import random

def downloadArquivo(nome):
    tempo = random.randint(1, 5)  # tempo aleatório entre 1 e 5 segundos
    print(f"Download iniciado de {nome}, tempo previsto: {tempo}s")
    time.sleep(tempo)  # simula o tempo de download
    print(f"Download {nome} concluído!")

# Lista de arquivos
arquivos = ["imagem1.jpg", "imagem2.jpg", "imagem3.jpg"]

# Lista para guardar as threads
threads = []

# Criar uma thread para cada arquivo
for arquivo in arquivos:
    inicio = threading.Thread(target=downloadArquivo, args=(arquivo,))
    threads.append(inicio)
    inicio.start()

# Esperar todas as threads terminarem
for inicio in threads:
    inicio.join()

print("Todos os downloads foram concluídos!")
