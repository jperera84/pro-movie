# Media Trailer Site

The project consists in a server side code to store a list of your favourite movies and TV Shows, including some useful
information for Movies and TVShows like Title, posters, and trailers.
The Main.py file will generate a static web page allowing visitors to browse their movies, tv shows and watch the trailers.

## Why this project?

This project was develop as Final Project for the course <i>"Programming Foundations with Python"</i> for the <i>Full Stack Web 
Developer nanodegree (UDACITY)</i>.

## Project code detail

The project consists in the following modules:

<ul>
  <li>main.py</li>
  <li>render_page.py</li>
  <li>content.py</li>
  <li>media.py</li>
  <li>movie.py</li>
  <li>tvshow.py</li>
</ul>

The classes: Media, Movie and TVShow are the Objects that stored the Movies and the TVShow, and those are being render in 
the <i>render_page.py</i> module.

In the <i>main.py</i> module you can create more movies or tv show and add it to the list of medias and those will be added to
the web page.

The project was developed using Python 2.7.12.

## Steps to run the program:

<ol>
  <li>Install Python 2.7.12 </li>
  <li>Edit the main.py file to add, edit or remove media objects.</li>
  <li>Run the main.py file</li>
</ol>

## Expected results

The project will be interpreted by the Python interpreter and when the parser finish the program will open a new browser tab
with the web page.

## Known issues
<ol>
  <li>The search option is not implemented yet.</li>
  <li>There is an error in the JSON parse that failed to show the information dialog when the Storyline attribute or the title has a word with Apostrophe (').</li>
</ol>
