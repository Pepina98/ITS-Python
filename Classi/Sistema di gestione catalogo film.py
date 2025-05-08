class MovieCatalog:
    def __init__(self):
        self.catalog: dict[str, list[str]] = {}

        #catalog: dict[str, list[str]] = {} scritta così è un attributo della Classe
        #catalog: dict[str, list[str]] scritta così è un attributo d'istanza
    
    def add_movie(self, director_name:str, movies:list[str]) -> None:
        if director_name not in self.catalog:
            self.catalog[director_name] = movies
        else:
            for movie in movies:
                if movie not in self.catalog[director_name]:
                    self.catalog[director_name].append(movie)

    def remove_movie(self, director_name:str, movie_name:str) -> None:
        if director_name in self.catalog and movie_name in self.catalog[director_name]:
            self.catalog[director_name].remove(movie_name)
            if not self.catalog[director_name]:
                del self.catalog[director_name]
        
        # nelle liste se si mette if nome della lista si controlla che la lista è piena
        # nelle liste se si mette if not nome della lista si controlla che la lista è vuota

    def list_directors(self) -> list[str]:
        return list(self.catalog.keys())

    def get_movie_by_director(self, director_name:str) ->list[str]: #delle volte un metodo può ritornare diverse tipologie di return quindi si aggiunge tra una tipologia e un'altra | (or)
        if director_name in self.catalog:                           # es  -> list[str] | str:
            return self.catalog[director_name]
        
    def search_movies_by_title(self, title:str) -> dict[str, list[str]] | str:
        result: dict[str, list[str]] = {}

        for director, movies in self.catalog.items():
            matching_movies: list[str] = []

            for movie in movies:
                if movie.lower() == title.lower():
                    matching_movies.append(movie)

            if matching_movies:
                result[director] = matching_movies
        
        if result:
            return result
        else:
            return "Nessun film trovato"
        

catalog = MovieCatalog()

'''
qui aggiungere catalog.add_movie, catalog.remove_movie, catalog.list_director
catalogget_movie_by_director, catalog.search_movies_by_title e i rispettivi print
        
'''

'''
Ereditarietà

class Media:
    def __init__(self, title:str, year:int) -> None:
        self.title = title
        self.year = year

    def get_info(self) -> str:
        return f'{self.title} ({self.year})'

class Movie(Media):
    def __init__(self, title:str, year:int, duration:int):
        super().__init__(title, year)
        self.duration = duration
    
    def get_info(self) -> str:
        return f'[FILM] {super().get_info()} - Durata: {self.duration}'

class SerieTV(Media):
    def __init__(self, title:str, year:int, seasons:int):
        super().__init__(title, year)
        self.seasons = seasons 

    def get_info(self) -> str:
        return f'[SERIETV] {super().get_info()} - Seasons: {self.seasons}'

'''
