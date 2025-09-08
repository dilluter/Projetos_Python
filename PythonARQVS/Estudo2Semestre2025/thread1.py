import threading   # Módulo que permite trabalhar com threads em Python
import time        # Módulo usado para simular tempo de processamento

# Função que será executada pela primeira thread
def imprimir_1_a_10():
    """
    Esta função imprime os números de 1 a 10.
    Utiliza time.sleep() para simular um tempo de processamento entre cada número.
    """
    for i in range(1, 11):  # Loop de 1 até 10 (inclusive)
        print(f"[Thread-1] Número: {i}")
        time.sleep(0.5)  # Espera de meio segundo para simular processamento

# Função que será executada pela segunda thread
def imprimir_50_a_60():
    """
    Esta função imprime os números de 50 a 60.
    Também utiliza time.sleep() para simular tempo de processamento.
    """
    for i in range(50, 61):  # Loop de 50 até 60 (inclusive)
        print(f"[Thread-2] Número: {i}")
        time.sleep(0.5)

# Ponto de entrada do programa
if __name__ == "__main__":
    # Criamos duas threads, cada uma executando uma das funções acima
    thread1 = threading.Thread(target=imprimir_1_a_10)
    thread2 = threading.Thread(target=imprimir_50_a_60)

    # Iniciamos as threads (executam em paralelo)
    thread1.start()
    thread2.start()

    # Usamos join() para aguardar a finalização das duas threads
    # Isso garante que o programa só termine quando ambas tiverem acabado
    thread1.join()
    thread2.join()

    print("Programa finalizado! Todas as threads terminaram.")
