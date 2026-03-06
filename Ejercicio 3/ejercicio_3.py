# Programa de juego de adivinar un número

import random

pc_number = random.randint(1, 100)
player_number = 0
fallas = 1

print()
print("Bienvenido al juego de adivinar el número!")
print("Estoy pensando en un número entre 1 y 100, ¿puedes adivinar cuál es?")
player_number = int(input("Ingresa tu número: "))

if player_number > 100 or player_number < 1:
    print("Número inválido, por favor ingresa un número entre 1 y 100")
    exit()
while player_number != pc_number:
    print()
    if player_number < pc_number:
        print("El número es mayor que", player_number)
    else:
        print("El número es menor que", player_number)
    player_number = int(input("Ingresa tu número: "))
    fallas += 1
print("Felicidades! adivinaste el número!!")
print("Lo lograste en: " + str(fallas) + " intentos ")
exit()

