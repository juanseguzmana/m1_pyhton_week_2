employees = int(input("¿Cuántos empleados? "))
for employee in range(employees):
    print(f"\nEmpleado {employee + 1}:")   
    name = input("Nombre: ")
    sales = []
    for i in range(3):
        sale = float(input(f"Ventas {i + 1}: "))
        sales.append(sale)
    average = sum(sales) / 3
    if average >= 6:
        rating = "Excelente"
    elif average >= 3:
        rating = "Bien"
    else:
        rating = "Bajo rendimiento"
    print(f"{name}: {rating}")