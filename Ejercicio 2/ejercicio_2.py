# Programa de juego

import random
vida = 50

while True:
    daño = random.randint(5, 15)
    vida = vida - daño

    print("El jefe te ha quitado :", daño, "HP")
    print("Tu vida es de:", vida)

    if vida <= 0:
        print("Haz sido eliminado")
        break