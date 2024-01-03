import threading
import subprocess
from multiprocessing import process
import time


def coisa_1():
    while True:
        subprocess.run(["python", "principal.py"])


def coisa_2():
    while True:
        subprocess.run(["python", "canva.py"])


thread_1 = threading.Thread(target=coisa_1)
thread_2 = threading.Thread(target=coisa_2)


thread_1.start()
thread_2.start()

# def funcao_1():
# while True:
#   subprocess.run(["python", "principal.py"])
