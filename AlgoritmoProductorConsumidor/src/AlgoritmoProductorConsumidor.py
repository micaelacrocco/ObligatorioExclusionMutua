import time
from colorama import Fore, Style, init
from src.__init__ import cola_pizzas

# Productor
def chef():
    for i in range(1, 11):
        pizza = f'Pizza-{i}'
        cola_pizzas.put(pizza)
        print(Fore.GREEN + f'Chef: Preparada {pizza}' + Style.RESET_ALL)
        time.sleep(1)

# Consumidor
def repartidor():
    for x in range(10):
        pizza = cola_pizzas.get()
        print(Fore.BLUE + f'Repartidor: Entregando {pizza}...' + Style.RESET_ALL)
        time.sleep(2)
        cola_pizzas.task_done()

