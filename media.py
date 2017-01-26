""" This module provide the media class """
class Media(object):
    """ This clas provide the data structure necessary to manage media objects """
    def __init__(self, title, poster_url, storyline, trailer_url, genre):
        self.title = title
        self.poster_url = poster_url
        self.storyline = storyline
        self.trailer_url = trailer_url
        self.genre = genre
