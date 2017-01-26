""" Testing Program """
import movie

MATRIX = movie.Movie("Matrix", "https://wikipedia.com", "The matrix comment", "https://youtube.com",
                     "Sciencie Fiction", "Martin Scorceses", "1:55", "PG-13", "1998-01-01")

print MATRIX.storyline
