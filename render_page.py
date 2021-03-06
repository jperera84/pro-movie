""" This module provide functions to render the web page """
import webbrowser
import os
import re
import json
import movie
import content


# Main page content and scripting
MAIN_PAGE_CONTENT = """
  <!DOCTYPE html>
  <html>
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, minimum-scale=1.0, initial-scale=1.0, user-scalable=yes">
      <meta name="theme-color" content="#F9FBE7">
      <title>Media Trailer Site</title>
      <link href='https://fonts.googleapis.com/css?family=Roboto' rel='stylesheet' type='text/css'>
      <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
      <style>
        * {
            box-sizing: border-box;
        }
        html, body{
          padding: 0;
          margin: 0;
          background: #FAFAFA;
          font-family: 'Roboto', sans-serif;
        }
        .header{
          width: 100%;
          height: 56px;
          box-shadow: 0 2px 4px rgba(0, 0, 0, 0.4);
          background: #CDDC39;
          color: #000;
          display: flex;
          flex-direction: row;
          align-items: center;
          padding: 0 16px;
        }
        .header__menu-toogle{
          background: none;
          border: none;
          width: 24px;
          height: 24px;
          padding: 0;
          margin: 0;
          color: #827717;
        }
        .header__site-name{
          flex: 1;
          font-size: 20px;
          padding: 0 16px;
        }
        a{
          font-size: 14px;
          text-decoration: none;
        }
        .container{
          display: flex;
          flex-direction: column;
          max-width: 760px;
          min-width: 200px;
          margin-top: 8px;
          margin-left: auto;
          margin-right: auto;
          padding: 8px;
        }
        .container__option-box{
          display: flex;
          flex-direction: row;
          flex-wrap: wrap;
          width: 100%;
          height: auto;
          min-height: 56px;
          border-radius: 3px;
          box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 1px 5px 0 rgba(0, 0, 0, 0.12), 0 3px 1px -2px rgba(0, 0, 0, 0.2);
          align-items: center;
        }
        .container__option-box-button{
          flex: 1;
          border: none;
          background-color: #CDDC39;
          box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 1px 5px 0 rgba(0, 0, 0, 0.12), 0 3px 1px -2px rgba(0, 0, 0, 0.2);
          border-radius: 3px;
          color: #000;
          height: 32px;
          max-width: 80px;
          margin: 0 8px;
          outline: none;
        }
        .container__option-box-button:hover{
          background-color: #9E9D24;
        }
        .container__option-box-box-input{
          display: flex;
          flex: 1;
          align-items: center;
          margin-left: 8px;
          margin-right: 8px;
        }
        .container__option-box-input{
          border: none;
          border-color: transparent;
          background: none;
          border-bottom-style: solid;
          height: 32px;
          border-bottom: solid 1px #827717;
          outline: none;
          max-width: 120px;
        }
        .container__movies{
          display: flex;
          flex-direction: column;
          width: 100%;
          height: 90vh;
          overflow-y: auto;
        }
        .container__tvshow{
          display: flex;
          flex-direction: column;
          width: 100%;
          height: 90vh;
          overflow-y: auto;
        }
        .box-hidden{
          display: none;
        }
        .card {
          display: flex;
          flex-direction: row;
          box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 1px 5px 0 rgba(0, 0, 0, 0.12), 0 3px 1px -2px rgba(0, 0, 0, 0.2);
          padding: 8px;
          margin-top: 16px;
          border-radius: 3px;
          background-color: #F9FBE7;
          color: #000;
          width: 100%;
          height: auto;
          min-height: 120px;
        }
        .container__movies-poster{
          border-radius: 3px;
          width: 80px;
          height: 110px;
        }
        .container__movies-content{
          display: flex;
          flex: 1;
          flex-direction: column;
          padding: 0 8px;
          vertical-align: top;
        }
        .container__movies-like{
          min-width: 48px;
        }
        span.title{
          font-size: 18px;
        }
        span.date{
          padding: 8px 0;
          font-size: 12px;
        }
        span.storyline{
          height: 40px;
          display:inline-block;
          text-overflow:ellipsis;
          overflow:hidden;
          font-size: 12px;
        }
        .container__movies-trailer{
          width: auto;
          padding: 8px 0;
          border: none;
          background: none;
          align-self: flex-end;
          outline: none;
          color: #827717;
          cursor: pointer;
          padding: 8px 8px;
        }
        .container__movies-trailer:hover{
          color: #AFB42B;
        }
        .trailer-modal{
          transition: opacity 400ms ease-in;
          position: fixed;
          top: 0;
          right: 0;
          bottom: 0;
          left: 0;
          z-index: 99999;
          opacity:0;
          background: rgba(0, 0, 0, 0.8);
          pointer-events: none;
          height: auto;
        }
        .trailer-modal-target{
          opacity: 1;
          pointer-events: auto;
        }
        .trailer-modal > div {
            position: relative;
            max-width: 600px;
            min-height: 300px;
            height: auto;
            border-radius: 3px;
            background: #F9FBE7;
            box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 1px 5px 0 rgba(0, 0, 0, 0.12), 0 3px 1px -2px rgba(0, 0, 0, 0.2);
            margin: 10% auto;
        }
        .trailer-modal-content{
          display: flex;
          flex-direction: row;
          flex-wrap: wrap;
          padding: 16px;
        }
        .trailer-modal-content-info{
          display: flex;
          flex: 1;
          flex-direction: column;
          min-width: 200px;
          width: auto;
          height: auto;
          padding: 8px;
        }
        .trailer-modal-player{
          padding: 8px;
        }
        iframe{
          width: 100%;
          min-height: 200px;
          height: auto;
        }
        span.storylineinfo{
          height: 120px;
          display:inline-block;
          text-overflow:ellipsis;
          overflow:hidden;
          font-size: 12px;
        }
        span.raiting{
          display:inline-block;
          font-size: 12px;
        }
        .close-player{
          border: none;
          background-color: #CDDC39;
          box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 1px 5px 0 rgba(0, 0, 0, 0.12), 0 3px 1px -2px rgba(0, 0, 0, 0.2);
          border-radius: 3px;
          color: #000;
          height: 32px;
          max-width: 80px;
          margin: 8px 0;
          outline: none;
        }
        .close-player:hover{
          color: #AFB42B;
        }
      </style>
    </head>
    <body>
      <div class="header">
        <button class="header__menu-toogle material-icons">menu</button>
        <p class="header__site-name">Media Site</p>
        <a href="#">Welcome guest</a>
      </div>
      <div class="container">
        <div class="container__option-box">
          <div class="container__option-box-box-input">
            <input type="text" id="search" class="container__option-box-input" placeholder="Search for media..."></input>
            <button class="header__menu-toogle material-icons">search</button>
          </div>
          <button class="container__option-box-button" id="btMoview">Movies</button>
          <button class="container__option-box-button" id="btTvShow">TV Shows</button>
        </div>
        <h4>Browse Media list</h4>
        <div class="container__movies" id="movieContainer">
          {{tiles}}
        </div>
        <div class="container__tvshow box-hidden" id="tvContainer">
          <div class="card">
            {{tvshowitems}}
          </div>
        </div>
      </div>

      <div id="trailerContainer" class="trailer-modal">
        <div class="trailer-modal-content">
          <div class="trailer-modal-content-info">
            <span class="title" id="playerTitle"></span>
            <span class="date" id="playerDate"></span>
            <span class="storylineinfo" id="playerStoryLine"></span>
            <span class="raiting" id="playerRaiting"></span>
            <button class="close-player">Close</button>
          </div>
          <div class="trailer-modal-player">
            <iframe id="player" src=""></iframe>
          </div>
        </div>
      </div>

      <script>
        btMovie = document.getElementById('btMoview');
        btTvShow = document.getElementById('btTvShow');
        function toogleList(e){
            let divMovie = document.querySelector('.container__movies');
            let divTvShow = document.querySelector('.container__tvshow');
            if(divMovie.className.includes("box-hidden")){
              divMovie.className = "container__movies";
              divTvShow.className = "container__tvshow box-hidden";
            }else{
              divMovie.className = "container__movies box-hidden";
              divTvShow.className = "container__tvshow";
            }
        }
        btMovie.addEventListener("click", toogleList, false);
        btTvShow.addEventListener("click", toogleList, false);
        arrayButtons = document.querySelectorAll('.container__movies-trailer');
        function showDialog(e){
          var target = e.target;
          let data = target.getAttribute("data-to-show");

          let media = JSON.parse(data);
          let playerTitle = document.getElementById('playerTitle');
          playerTitle.textContent = media.title;
          let playerDate = document.getElementById('playerDate');
          playerDate.innerHTML = "<b>Release date:</b>" + media.date;
          let playerStoryLine = document.getElementById('playerStoryLine');
          playerStoryLine.textContent = media.storyline;
          let playerRaiting = document.getElementById('playerRaiting');
          playerRaiting.innerHTML = "<b>Raiting:</b>" + media.raiting;
          let player = document.getElementById('player');
          player.src = media.youtubeurl;

          let dialog = document.querySelector('.trailer-modal');
          dialog.classList.add('trailer-modal-target');
        }
        for(let i = 0; i < arrayButtons.length; i++){
          arrayButtons[i].addEventListener("click", showDialog, false);
        }
        btClosePlayer = document.querySelector('.close-player');
        function closeDialog(e){
          var target = e.target;
          let player = document.getElementById('player');
          player.src = "";
          let dialog = document.querySelector('.trailer-modal');
          dialog.classList.remove('trailer-modal-target');
        }
        btClosePlayer.addEventListener("click", closeDialog, false);
      </script>
    </body>
  </html>
"""
# A single movie entry html template
MEDIA_CONTENT = """
  <div class="card">
      <img src="{{poster}}" alt="Poster" class="container__movies-poster">
      <div class="container__movies-content">
        <span class="title">{{title}}</span>
        <span class="date"><b>Release date:</b> {{releasedate}}</span>
        <span class="storyline">{{storyline}}</span>
        <button data-to-show='{{json}}' class="container__movies-trailer">Watch Trailer</button>
      </div>
      <div class="container__movies-like">
        <button class="header__menu-toogle material-icons">favorite_border</button>
      </div>
  </div>
"""

# Single function to inject content into html
def create_media_card(objs):
    """Single function to inject content into html"""
    contentaux = ''
    movies = []
    tvshows = []
    for item in objs:
        if isinstance(item, movie.Movie):
            movies.append(item)
        else:
            tvshows.append(item)
    for mov in movies:
        tile = MEDIA_CONTENT
        jsonobj = content.Content()
        jsonobj.title = mov.title
        jsonobj.date = mov.release_date
        jsonobj.storyline = re.sub("\n", " ", mov.storyline)
        jsonobj.youtubeurl = mov.trailer_url
        jsonobj.raiting = mov.rating
        jsonstr = json.dumps(jsonobj.__dict__)
        tile = tile.replace("{{poster}}", mov.poster_url)
        tile = tile.replace("{{title}}", mov.title)
        tile = tile.replace("{{releasedate}}", mov.release_date)
        tile = tile.replace("{{storyline}}", mov.storyline)
        tile = tile.replace("{{json}}", jsonstr)
        contentaux = contentaux + " " + tile

    rendered_content = re.sub("{{tiles}}", contentaux, MAIN_PAGE_CONTENT)
    contentaux = ''
    for tvshow in tvshows:
        tileshow = MEDIA_CONTENT
        jsonobj = content.Content()
        jsonobj.title = tvshow.title
        jsonobj.date = tvshow.premiere_date
        jsonobj.storyline = re.sub("\n", " ", tvshow.storyline)
        jsonobj.youtubeurl = tvshow.trailer_url
        jsonstr = json.dumps(jsonobj.__dict__)
        tileshow = tileshow.replace("{{poster}}", tvshow.poster_url)
        tileshow = tileshow.replace("{{title}}", tvshow.title)
        tileshow = tileshow.replace("{{releasedate}}", tvshow.premiere_date)
        tileshow = tileshow.replace("{{storyline}}", tvshow.storyline)
        tileshow = tileshow.replace("{{json}}", jsonstr)
        contentaux = contentaux + " " + tileshow
    rendered_content = re.sub("{{tvshowitems}}", contentaux, rendered_content)
    return rendered_content

# Single function to create and open the page in the browser
def open_media_page(objs):
    """ Single function to create and open the page in the browser """
    output_file = open('index.html', 'w')

    output_file.write(create_media_card(objs))
    output_file.close()

    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)




