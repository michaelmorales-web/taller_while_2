# Programa de calculo de rebotes

print("-----------------------------------")
print("---------Bienvenido----------------")
print("-----------------------------------")

h = input("Ingrese el valor de h:")
n = 0
q = h//5

while h > q :
    h = h - 0.1 * h
    n = n + 1

print("-------------------------------")
print("El numero de veces que la pelota va a rebotar antes de que deje de saltar su quinta parte")
print("-------------------------------")