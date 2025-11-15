students = int(input("Cuantos estudiantes? "))
for student in range(students):
    print(f"\nEstudiante {student +1}: ")
    notes = []
    for i in range(3):
        note = float(input(f"Nota {i + 1}: "))
        notes.append(note) 
    average = sum(notes) / 3
    status = "Aprobado" if average >= 3.0 else "Reprobado"
    print(f"Promedio: {average: 1f} - {status}")