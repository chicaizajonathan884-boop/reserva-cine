# Reserva de un asiento en una sala de cine

asientos = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]

fila = int(input("Ingrese la fila (0-2): "))
columna = int(input("Ingrese la columna (0-3): "))

asientos[fila][columna] = 1

print("Estado de la sala:")

for fila in asientos:
    for asiento in fila:
        print(asiento, end=" ")
    print()