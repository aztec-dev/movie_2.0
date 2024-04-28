"""(Incomplete) Tests for MovieCollection class."""
from movie import Movie
from moviecollection import MovieCollection


def run_tests():
    """Test MovieCollection class."""

    # Test empty MovieCollection (defaults)
    print("Test empty MovieCollection:")
    movie_collection = MovieCollection()
    print(movie_collection)
    assert not movie_collection.movies  # An empty list is considered False

    # Test loading movies
    print("Test loading movies:")
    movie_collection.load_movies("movies.json")
    print(movie_collection)
    assert movie_collection.movies  # Assuming file is non-empty; non-empty list is considered True

    # Test adding a new Movie with values
    print("Test adding new movie:")
    movie_collection.add_movie(Movie("Amazing Grace", 2006, "Drama", False))
    print(movie_collection)

    # Test sorting movies
    print("Test sorting - year:")
    movie_collection.sort('year')
    print(movie_collection)

    # Test sorting movies for title
    print("Test sorting - title")
    movie_collection.sort('title')
    print(movie_collection)

    # Test sorting movies for is watched
    print("Test sorting - is_watched")
    movie_collection.sort('is_watched')

    # Test saving movies
    print("Test saving movies")
    movie_collection.save_movies("movies.json")
    print(movie_collection)

    # Test watched movies
    print("Test get number of watched movies")
    print(movie_collection.get_watched())

    # Test unwatched movies
    print("Test get number of unwatched movies")
    print(movie_collection.get_unwatched())


run_tests()
