"""
Name: Azariah Punndari
Date: 27th November 2022
Brief Project Description: This program uses the kivy library to build a GUI program that display, add, clear and save
movies into a .json file
GitHub URL: https://github.com/cp1404-students/a2-movies-azariahpundari1
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.uix.button import Button

from moviecollection import MovieCollection
from movie import Movie

FILENAME = 'movies.json'
MOVIE_KEY = {'Title': 'title', 'Year': 'year', 'Category': 'category', "Watched": 'is_watched'}
CATEGORIES = ["Action", "Comedy", "Drama", "Thriller", "Other"]
WATCHED_COLOR = (1, 1, 0, 1)  # Aqua Green (like sample)
UNWATCHED_COLOUR = (0, 1, 1, 1)  # Yellow

# Pycharm suggests to make this method static, this was done to remove green squiggly line - doesn't affect program
def are_valid_input(title, year, category):
    """Return False & a string if title, year & category inputs are not valid"""
    if title == '' or year == '' or category == '':
        return False, 'All fields must be completed'
    try:
        year = int(year)
        if year < 0:
            return False, 'Year must be >= 0'
        if category not in CATEGORIES:
            return False, 'Category must be one of ' + ", ".join(CATEGORIES)
    except ValueError:
        return False, 'Please enter valid year'
    return True, ''


class MoviesToWatchApp(App):
    """Main program - Movies to watch app"""
    sort_key = StringProperty()
    status_text = StringProperty()
    watch_status = StringProperty()
    sort_option = ListProperty()

    def __init__(self, **kwargs):
        """Construct main app"""
        super().__init__(**kwargs)
        self.movie_collection = MovieCollection()
        self.movie_collection.load_movies(FILENAME)

    def build(self):
        """Build kivy GUI"""
        self.title = 'Movies To Watch 2.0'
        self.root = Builder.load_file('app.kv')
        self.sort_option = sorted(MOVIE_KEY.keys())  # Sort movie by given key - eg: 'year'
        self.sort_key = self.sort_option[0]  # sets default sorting to 'category'
        self.status_text = ""  # set blank for 'output' in Label
        return self.root

    def update_movie_buttons(self):
        """Update button to display a new movie label and different button color"""
        self.root.ids.load_box.clear_widgets()
        self.create_movie_widgets()
        self.display_movie_counts()

    def update_sorting(self):
        """Sort movie according to key"""
        sort = self.root.ids.sort_selection.text
        self.movie_collection.sort(MOVIE_KEY[sort])
        self.root.ids.output.clear_widgets()
        self.update_movie_buttons()

    def create_movie_widgets(self):
        """Create buttons from list of movie collection and add them to GUI"""
        for movie in self.movie_collection.movies:
            if not movie.is_watched:
                temp_button = Button(text=str(movie), background_color=UNWATCHED_COLOUR)
            else:
                temp_button = Button(text=str(movie), background_color=WATCHED_COLOR)
            temp_button.bind(on_release=self.press_entry)
            temp_button.movie = movie
            # Add the button to the "load_box" layout widget
            self.root.ids.load_box.add_widget(temp_button)

    def press_entry(self, instance):
        """Handle pressing movie button to get watched status"""
        # make it so that it clears current button and adds updated button
        movie = instance.movie
        if not movie.is_watched:
            self.status_text = movie.watched()
        else:
            self.status_text = movie.unwatched()
        instance.text = str(movie)
        self.update_movie_buttons()

    def display_movie_counts(self):
        """Display the number of watched & unwatched movies"""
        self.watch_status = f"To watch: {self.movie_collection.get_unwatched()}. " \
                            f"Watched: {self.movie_collection.get_watched()} "

    def clear_movies(self):
        """Clear all movie in kivy GUI"""
        self.movie_collection.movies.clear()
        self.update_movie_buttons()

    def clear_input_text(self):
        """Clear title, category and year text fields"""
        self.root.ids.input_title.text = ''
        self.root.ids.input_year.text = ''
        self.root.ids.input_category.text = ''

    def add_new_movie(self):
        """Add a new movie"""
        title = self.root.ids.input_title.text
        year = self.root.ids.input_year.text
        category = self.root.ids.input_category.text
        is_valid, error_message = are_valid_input(title, year, category)
        if not is_valid:
            self.status_text = error_message
            return
        new_movie = Movie(title, int(year), category, False)
        self.movie_collection.add_movie(new_movie)
        self.clear_input_text()
        self.update_movie_buttons()

    def on_stop(self):
        """Save current movies to file"""
        self.movie_collection.save_movies(FILENAME)


if __name__ == '__main__':
    MoviesToWatchApp().run()
