"""..."""
import json
from operator import attrgetter
from movie import Movie


class MovieCollection:
    def __init__(self):
        """Construct a Movie Collection class from a movie list."""
        self.movies = []

    def __str__(self):
        """Return a list of movies."""
        return f"{self.movies}"

    # def __repr__(self):
    #     """Return list of movies with variables"""
    #     return vars(self)

    def load_movies(self, file_name):
        """Load movies from a specified file"""
        with open(file_name, 'r') as in_file:
            records = json.load(in_file)
        for record in records:
            self.movies.append(Movie(**record))
        # print(f"{len(self.movies)} movies loaded from movies")
        # print(f"{self.movies[0]}")  # Test to see one of the movies

    def add_movie(self, movie):
        """Add a movie to existing movie collection."""
        self.movies.append(movie)

    def sort(self, attribute):
        """Sort the movie according to attribute passed in"""
        self.movies.sort(key=attrgetter(attribute))

    def save_movies(self, file_name):
        """Save movies to file name"""
        json_string = json.dumps(self.movies, default=vars)
        with open(file_name, 'w') as out_file:
            out_file.write(json_string)

    def get_watched(self):
        """Get number of watched movies"""
        watched_count = 0
        for i, movie in enumerate(self.movies):
            if movie.is_watched:  # is_watched = True
                watched_count += 1
        return watched_count

    def get_unwatched(self):
        """Get number of unwatched movies"""
        unwatched_count = 0
        for i, movie in enumerate(self.movies):
            if not movie.is_watched:  # is_watched = False
                unwatched_count += 1
        return unwatched_count
