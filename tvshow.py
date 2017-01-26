""" This module provide the tvshow class """
import media

class TvShow(media.Media):
    """ This clas provide the data structure necessary to manage TvShow objects """
    def __init__(self, title, poster_url, storyline, trailer_url, genre,
                 season_no, episodes_no, created_by, running_time, tv_channel, premiere_date):
        media.Media.__init__(title, poster_url, storyline, trailer_url, genre)
        self.season_no = season_no
        self.episodes_no = episodes_no
        self.created_by = created_by
        self.running_time = running_time
        self.tv_channel = tv_channel
        self.premiere_date = premiere_date

