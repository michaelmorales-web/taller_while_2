print("------------------")
print("bienvenido")
print("-------------------")
c1 = float(input("Capital de Pedro: "))
c2 = float(input("Capital de Juan: "))
c3 = float(input("Capital necesario para el negocio: "))

meses = 0

while (c1 + c2) < c3:
    c1 = c1 + 0.03 * c1
    c2 = c2 + 0.04 * c2
    meses = meses + 1

print()
print("procesando")
print()

print()
print("resultados")
print()
print(f"Felicidades! Podrán hacer el negocio en, {meses} meses!")