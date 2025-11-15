movies = []
quantity = int(input("Ingrese la cantidad de peliculas: "))
for i in range(quantity):
    duration = int(input("Duración de la pelicula (min): "))
    if duration < 100:
        movie_type = "Corta"
    elif duration <= 150:
        movie_type = "Media"
    else:
        movie_type = "Larga"
    movies.append(f"{duration} min - {movie_type}")
    print(f"Pelicula agregada: {movie_type}")
print("\nLista de peliculas")
for movie in movies:
    print(movie)