genres = []
repeated_genres = []
quantity = int(input("Ingrese la cantidad de canciones: "))
for i in range(quantity):
    genre = input("Ingrese el genero musical: ").lower()
    if genre in genres:
        if genre not in repeated_genres:
            repeated_genres.append(genre)
    else:
        genres.append(genre)
print("\nGeneros encontrados: ")
for genre in genres:
    print(f"- {genre}")
if repeated_genres:
    print("\nGeneros repetidos: ")
    for genre in repeated_genres:
        print(f"- {genre}")