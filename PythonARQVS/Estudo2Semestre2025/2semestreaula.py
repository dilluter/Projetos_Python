import threading
import time
import math
from concurrent.futures import thread


def estrutura(nome, inicio, fim):
    for i in range(inicio, fim + 1):
        print(F"{nome} -> {i}")
        time.sleep(1)
        thread1 = threading.Thread(target=estrutura, args=("thread1", 1, 90))
        thread2 = threading.Thread(target=estrutura, args=("thread1", 1, 90))
        thread1.start()
        thread.join