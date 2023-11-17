from src.AlgoritmoProductorConsumidor import chef, repartidor
import threading
from colorama import Fore, Style, init

def main():
    # Hilos para productor y consumidor
    hilo_chef = threading.Thread(target=chef)
    hilo_repartidor = threading.Thread(target=repartidor)

    # Inicio de los hilos
    hilo_chef.start()
    hilo_repartidor.start()

    # Esperar a que los hilos terminen
    hilo_chef.join()
    hilo_repartidor.join()

    print(Fore.YELLOW + "La pizzería ha terminado de operar por hoy" + Style.RESET_ALL)

if __name__ == "__main__":
    main()