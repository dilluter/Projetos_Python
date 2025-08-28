import threading
import time

# Função que simula um contador
def contar():
    for i in range(1, 6):
        print(f"Contador: {i}")
        time.sleep(1)  # pausa 1 segundo

# Função que simula mensagens no sistema
def mensagens():
    for i in range(1, 6):
        print(f"Mensagem {i}")
        time.sleep(0.7)  # pausa 0.7 segundos

# Criando as threads
t1 = threading.Thread(target=contar)
t2 = threading.Thread(target=mensagens)

# Iniciando as threads
t1.start()
t2.start()

# Esperando ambas terminarem
t1.join()
t2.join()

print("Programa finalizado!")
