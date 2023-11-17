import time
from colorama import Fore, Style, init
from src.__init__ import choosing, number

def tomar_numero(id_proceso):
    choosing[id_proceso] = True
    number[id_proceso] = max(number) + 1
    choosing[id_proceso] = False

    print(Fore.GREEN + f"Cliente {id_proceso} tomó el número {number[id_proceso]}" + Style.RESET_ALL)

def entrar_a_region_critica(id_proceso):
    for otro_proceso in range(len(number)):
        while choosing[otro_proceso]:
            pass  # Espera activa

        while (number[otro_proceso] != 0 and 
                ((number[id_proceso], id_proceso) > (number[otro_proceso], otro_proceso))):
            pass  # Espera activa

    # Sección crítica (mostrador de la oficina de correos)
    print(Fore.BLUE + f"     Cliente {id_proceso} está siendo atendido en el mostrador" + Style.RESET_ALL)
    time.sleep(2)  # Simula trabajo en la región crítica
    print(Fore.BLUE + f"     Cliente {id_proceso} ha sido atendido y sale del mostrador" + Style.RESET_ALL)

    # Salida de la región crítica
    number[id_proceso] = 0

def cliente(id_proceso):
    while True:
        tomar_numero(id_proceso)
        entrar_a_region_critica(id_proceso)
        time.sleep(3)