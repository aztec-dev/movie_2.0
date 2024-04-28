"""..."""


# TODO: Create your Movie class in this file


class Movie:
    """Represent a Movie object"""

    def __init__(self, title="", year=0, category="", is_watched=False):
        """Construct a Movie instance based on movie year, category, title & watch status"""
        self.title = title
        self.year = year
        self.category = category
        self.is_watched = is_watched

    def __str__(self):
        """Return a string displaying movie title, category & year"""
        return f"{self.title} ({self.category} from {self.year}) {'watched' if self.is_watched else ''}"

    def __repr__(self):
        """Return list of movies with variables"""
        return vars(self)

    def watched(self):
        """Mark the movie as watched"""
        self.is_watched = True
        return f"You have watched {self.title}"

    def unwatched(self):
        """Mark the movie as unwatched"""
        self.is_watched = False
        return f"You need to watch {self.title}"
