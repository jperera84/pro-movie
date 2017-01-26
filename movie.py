""" This module provide the movie class """
import media

class Movie(media.Media):
    """ This clas provide the data structure necessary to manage movie objects """
    def __init__(self, title, poster_url, storyline, trailer_url, genre,
                 directed_by, duration, rating, release_date):
        media.Media.__init__(self, title, poster_url, storyline, trailer_url, genre)
        self.directed_by = directed_by
        self.duration = duration
        self.rating = rating
        self.release_date = release_date

