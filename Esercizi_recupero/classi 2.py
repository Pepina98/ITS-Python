
class Movie:

    def __init__(self, movie_id:str, title:str, director:str, is_rented = False):
        self.movie_id: str = movie_id
        self.title: str = title
        self.director: str = director
        self.is_rented: bool = is_rented

    def rent(self) -> None:
        if self.is_rented == True:
            print(f"Il film {self.title} è già noleggiato.")
        else:
            self.is_rented == True

    def return_movie(self) -> None:
        if not self.is_rented == True:
            print(f"Il film {self.title} non è stato noleggiato da questo cliente.")
        else:
            self.is_rented == False 

class Costumer:
        
    def __init__ (self, costumer_id:str, name:str):
        self.costumer_id:str = costumer_id
        self.name:str = name
        self.rented_movies:list[Movie] = []

    def rent_movie(self, movie: Movie) -> None:
        if movie.is_rented == True:
            print(f"Il film {movie.title} è già noleggiato")
        
        else:
            movie.rent()
            self.rented_movies.append(movie)

    def return_movie(self, movie: Movie) -> None:
        if movie not in self.rented_movies:
            print(f"Il film {movie.title} non è stato noleggiato da questo cliente.")
        
        else:
            movie.return_movie()
            self.rented_movies.remove(movie)

class VideoRentalStore:

    def __init__(self):
        self.movies:dict[str, Movie] = {}
        self.costumers:dict[str, Costumer] = {}
        

    def add_movie (self, movie_id:str, title:str, director:str) -> None:
        
        if movie_id not in self.movies:
            movie: Movie = Movie(movie_id, title, director)
            self.movies[movie_id] = movie 

            tupla : tuple = (movie_id, movie)
            self.movies.update(tupla)

        else:
            print(f"Il film con ID {movie_id} esiste già.")

    def register_costumer(self, costumer_id:str, name:str) -> None:
        if costumer_id not in self.costumers:
            costumer : Costumer = Costumer(costumer_id, name)
            self.costumers[costumer_id] = costumer

        else:
            print(f"Il cliente con ID {costumer_id} è già registrato.")

    def rent_movie(self, costumer_id: str, movie_id: str) -> None:
        if movie_id in self.movies and costumer_id in self.costumers:
            movie: Movie = self.movies[movie_id]
            self.costumers[costumer_id].rent_movie(movie)  

        else:
            print("Cliente o film non trovato")  

    def return_movie(self, costumer_id: str, movie_id:str) -> None:
        if movie_id in self.movies and costumer_id in self.costumers:
            movie: Movie = self.movies[movie_id]
            self.costumers[costumer_id].return_movie(movie)

        else:
            print("Cliente o film non trovato")

    def get_rented_movies(self, costumer_id:str) -> list[Movie]:
        if costumer_id in self.costumers:
            return self.costumers[costumer_id].rented_movies
        
        else:
            print("Cliente non trovato")

    def get_all_movies(self) -> list[Movie]:
        film_noleggiati: list[Movie] = []
        
        for costumer in self.costumers.values():
            film_noleggiati += costumer.rented_movies

        return film_noleggiati 


    


    




        