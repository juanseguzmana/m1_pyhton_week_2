vehicles = int(input("¿Cuántos vehículos? "))
for vehicle in range(vehicles):
    print(f"\nVehiculo {vehicle + 1}: ")
    hours = int(input("Horas de trabajo: "))
    parts = int(input("Piezas cambiadas: "))
    hour_value = 20000
    part_value = 50000
    total_cost = (hours * hour_value) + (parts * part_value)
    complexity = "Compleja" if hours > 10 or parts > 4 else "Normal"
    print(f"Costo: ${total_cost} - {complexity}")