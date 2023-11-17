from src.AlgoritmoLamport import cliente
import threading

def main():
    hilos_clientes = []

    for i in range(5):
        hilo_cliente = threading.Thread(target=cliente, args=(i,))
        hilos_clientes.append(hilo_cliente)

    for hilo_cliente in hilos_clientes:
        hilo_cliente.start()

    for hilo_cliente in hilos_clientes:
        hilo_cliente.join()

if __name__ == "__main__":
    main()
