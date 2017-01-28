""" Testing Program """
import movie
import tvshow
import render_page

# Creating the media items to load in the page

MOVIE1 = movie.Movie("The girl on the train",
                     "https://upload.wikimedia.org/wikipedia/en/3/34/The_Girl_on_The_Train.jpg",
                     """The next time she rides the train, Rachel sees someone reading
                     the news on his tablet and the lead story is about a missing woman
                     named Megan Hipwell, the woman Rachel watches from the train whom
                     she exited the train to yell at about cheating on her husband.""",
                     "https://www.youtube.com/embed/KkoEE1i0CX8",
                     "Thriller", "Martin Scorceses", "1:55", "PG-13", "1998-01-01")

MOVIE2 = movie.Movie("The Matrix",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/The_Matrix_Poster.jpg/220px-The_Matrix_Poster.jpg",
                     """In the near future, a computer hacker named Neo discovers that all life
                     on Earth may be nothing more than an elaborate facade created
                     by a malevolent cyber-intelligence.""",
                     "https://www.youtube.com/embed/m8e-FF8MsqU",
                     "Thriller", "Lana Wachowski, Lilly Wachowski",
                     "1:55", "R", "March 31, 1999")

MOVIE3 = movie.Movie("Resident Evil: The Final Chapter",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/bf/Resident_Evil_The_Final_Chapter_poster.jpg/220px-Resident_Evil_The_Final_Chapter_poster.jpg",
                     """Picking up immediately after the events in Resident Evil: Retribution,
                     Alice is the only survivor of what was meant to be humanitys final
                     stand against the undead.""",
                     "https://www.youtube.com/embed/DNaurVGUesw",
                     "Fantasy/Action", "Paul W. S. Anderson",
                     "1:45", "R", "January 27, 2017")

MOVIE4 = movie.Movie("Split",
                     "https://upload.wikimedia.org/wikipedia/en/3/31/Split_%282017_film%29.jpg",
                     """While the mental divisions of those with dissociative identity
                     disorder have long fascinated and eluded science.""",
                     "https://www.youtube.com/embed/AT4yz244uS8",
                     "Thriller/Horror", "M. Night Shyamalan",
                     "1:45", "PG-13", "January 20, 2017")

MOVIE5 = movie.Movie("A Dog Purpose",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/bf/A_Dog%27s_Purpose_%28film%29.jpg/220px-A_Dog%27s_Purpose_%28film%29.jpg",
                     """A devoted dog (Josh Gad) discovers the meaning of its own existence
                     through the lives of the humans it teaches to laugh and love.""",
                     "https://www.youtube.com/embed/WBvftTVGnGI",
                     "Fantasy/Drama", "Lasse Hallstrom",
                     "1:45", "PG-13", "January 27, 2017")

TVSHOW1 = tvshow.TvShow("The Crown",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/18/The_Crown_Title_Card.jpg/250px-The_Crown_Title_Card.jpg",
                        """Netflix-original drama chronicles the life of Queen Elizabeth II""",
                        "https://www.youtube.com/embed/JWtnJjn6ng0",
                        "Biographic", 1, 10, "Peter Morgan", "0:45", "Netflix", "November 4, 2016")

MEDIAS = [MOVIE1, MOVIE2, MOVIE3, MOVIE4, MOVIE5, TVSHOW1]

#Calling the render page module to generate the html file
render_page.open_media_page(MEDIAS)
