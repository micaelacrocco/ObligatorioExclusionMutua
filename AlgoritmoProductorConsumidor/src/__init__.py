import queue
from colorama import init

# Inicializar colorama
init(autoreset=True)

# Tamaño máximo de pizzas en la mesa
cola_pizzas = queue.Queue(maxsize=5)