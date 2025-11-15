total_points = 0
weeks = int(input("¿Cuantas semanas desea registrar? "))
for week in range(weeks):
    days = int(input(f"¿Cuantos días entrenó en la semana {week + 1}? "))   
    if days >= 5:
        points = 10
    elif days >= 3:
        points = 5
    else:
        points = 2  
    total_points += points
    print(f"Semana {week + 1}: {days} dias → +{points} puntos")
print(f"\nPuntos totales acumulados: {total_points}")