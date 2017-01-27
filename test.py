""" Testing Program """
import movie
import render_page

MOVIE1 = movie.Movie("The girl on the train",
                     "https://upload.wikimedia.org/wikipedia/en/3/34/The_Girl_on_The_Train.jpg",
                     """The next time she rides the train, Rachel sees someone reading
                     the news on his tablet and the lead story is about a missing woman
                     named Megan Hipwell, the woman Rachel watches from the train whom
                     she exited the train to yell at about cheating on her husband.""",
                     "https://www.youtube.com/watch?v=KkoEE1i0CX8",
                     "Thriller", "Martin Scorceses", "1:55", "PG-13", "1998-01-01")

MEDIAS = []
MEDIAS.append(MOVIE1)
render_page.open_media_page(MEDIAS)
