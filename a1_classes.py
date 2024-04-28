"""
Name: Azariah Pundari
Date started: 24 november 2022
GitHub URL: https://github.com/cp1404-students/a1-movies-azariahpundari1
most of the unused methods have been commented out as they're no longer in use
"""

from movie import Movie
from moviecollection import MovieCollection

MAX_MOVIE_LENGTH = 80
MIN_LENGTH = 3
OFFSET = 2  # aligns print for better view
unwatched_offset = ' '


def main():
    """Initialize Movies 1.0 program that uses classes as a movie collection program"""
    FILE_NAME = 'movies.json'
    MENU = 'Menu:\nD - Display movies\nA - add new movie\nW - Watch a movie\nQ - Quit'

    print("Movies To Watch 1.0 - Azariah Pundari")
    movie_collection = MovieCollection()
    movie_collection.load_movies(FILE_NAME)
    # display menu
    print(f"{len(movie_collection.movies)} movies loaded from {FILE_NAME}")
    print(MENU)
    option = input(">>> ").upper()
    while option != 'Q':
        if option == 'D':
            # sort movies by year in ascending order
            movie_collection.sort('year')
            # display_movies(movies)  # display movies like assignment 2
            # This display movies similar to assignment 1
            # Notice this displays as Star Wars: Episode IV - A New Hope (Action from 1977) watched
            # as 'watched' is for kivy purposes
            for i, movie in enumerate(movie_collection.movies):
                if movie.is_watched:
                    print(f"{i + 1:>{MIN_LENGTH}}. {unwatched_offset} {movie}")
                else:
                    print(f"{i + 1:>{MIN_LENGTH}}. * {movie}")
            print(f"{movie_collection.get_watched()} movies watched, {movie_collection.get_unwatched()} movies "
                  f"yet to watch")
        elif option == 'A':
            movie_to_add = get_new_movie()
            movie_collection.add_movie(movie_to_add)
            print(f"{movie_to_add} added to movie list")
        elif option == 'W':
            # Asks for user input if there are movies to watch
            if movie_collection.get_unwatched() != 0:
                print("Enter the number of a movie to mark as watched")
                movie_to_watch = get_movie_to_watch(movie_collection.movies)
                if not movie_to_watch.is_watched:
                    print(f"{movie_to_watch.title} from {movie_to_watch.year} watched")
                    movie_to_watch.is_watched = True
                else:
                    print(f"You have already watched {movie_to_watch.title}")
            else:
                print("No more movies to watch")
        else:
            print("Invalid menu choice")
        print(MENU)
        option = input(">>> ").upper()
    print(f"{len(movie_collection.movies)} movies saved to {FILE_NAME}\nhave a nice day :)")
    movie_collection.save_movies(FILE_NAME)


# def count_unwatched_movies(movies):
#     """Count the number of movies that have a False value."""
# return len([movie for movie in movies if not movie.is_watched])
# return movie

def get_movie_to_watch(movies):
    """Get user input - determines if the value fits certain criteria"""
    is_valid_input = False
    movie_index = 0
    while not is_valid_input:
        try:
            movie_index = int(input(">>> "))
            if movie_index < 0:
                print("Number must be >= 1")
            elif movie_index > len(movies):
                print("Invalid movie number")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid (not an integer)")
    movie_to_watch = movies[movie_index - 1]
    return movie_to_watch


def get_new_movie():
    """Ask user for a new movie including: title, year & category"""
    categories = ["Action", "Comedy", "Drama", "Thriller", "Other"]
    title = input("Title: ")
    while title == "":
        print("Input cannot be blank")
        title = input("Title: ")
    is_valid_input = False
    year = 0  # PyCharm suggests to add this as a global variable from the return statement.
    while not is_valid_input:
        try:
            year = int(input("Year: "))
            while year <= 0:
                print("Number must be >= 1")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid input; enter a valid number")
    categories_string = ", ".join(categories)
    print(f"Categories available: {categories_string}")
    category = input("Category: ").title()
    # Checks if user category is in available categories
    if category not in categories:
        print(f"invalid category; adding {categories[4]}")
        category = categories[4]  # This is Other
    return Movie(title, year, category, False)


# def get_movie_string(movie):
#     """Returns movie in a string"""
#     return f"{movie[0]} ({movie[2]}) from {movie[1]})"


# def save_movies(movies, FILE_NAME):
#     """Opens file, writes to file - saves and closes file"""
#     out_file = open(FILE_NAME, 'w')
#     for i, movie in enumerate(movies):
#         str_movie = [str(movie) for movie in movie]
#         print(",".join(str_movie), file=out_file)
#     out_file.close()


# def display_movies(movies):
#     """Display movies in movies.csv"""
# watch_counter = 0  # counts how many movies were watched
# unwatched_counter = 0  # counts how many movies need to be watched
# for i, movie in enumerate(movies):
#     print(movie)
# if status == "u":
#     movie = Movie(name, year, genre, status)
#     print(movie)
#     # unwatched_counter += 1
# else:
#     print(f"{i + 1:>3}. {name:<47} - {year:<5} ({genre})")
# watch_counter += 1
# print(f"{watch_counter} movies watched, {unwatched_counter} movies still to watch")


# def load_movies(FILE_NAME):
#     movies = []
#     in_file = open(FILE_NAME, 'r')
#     for line in in_file:
#         movie = line.strip().split(',')
#         # convert year str to int, helps with sorting movies
#         movie[1] = int(movie[1])  # ignore error
#         movies.append(movie)  # creates movies lists of lists
#     in_file.close()
#     return movies


if __name__ == '__main__':
    main()
    # tests
    # save_movies([["movies", "2002", "action", "u"]], 'movies.csv')
