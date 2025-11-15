rooms = int(input("¿Cuantas habitaciones? "))
occupied = 0
free_rooms = []
for room in range(rooms):
    print(f"\nHabitacion {room + 1}:")
    room_number = input("Número de habitacion: ")
    occupied_input = input("¿Ocupada? (si/no): ").lower()   
    if occupied_input in ["si"]:
        occupied += 1
    else:
        free_rooms.append(room_number)
free = rooms - occupied
print(f"\n--- RESULTADOS ---")
print(f"Habitaciones ocupadas: {occupied}")
print(f"Habitaciones libres: {free}")
if free_rooms:
    print("\nHabitaciones libres:")
    for room in free_rooms:
        print(f"- {room}")
else:
    print("\nNo hay habitaciones libres")