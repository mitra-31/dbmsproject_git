from app import app,mysql,save_images,save_music
from flask import Flask,render_template,request,redirect,flash,session,url_for,current_app,jsonify
from flask_fontawesome import fontawesome_css
from playsound import playsound
import os

def artists():
    artists = []
    f = open('app/artists.txt','r')
    for line in f:
        artists.append(line.split(","))
    return artists






"""
    Music dashboard

"""
@app.route('/music',methods=["GET","POST"])
def dashboard():
    genre = [['pop','bg.jpg'],['jazz','jazz.jpg'],['devotional','dev.jpg'],['hip hop','hiphop.jpg'],['workout',"workout.jpg"],['sad','sad1.jpg'],['happy','happy.jpg'],["Melody","melody.jpg"]]
    artist = artists()
    return render_template("user_dashboard/music_dash.html",genres=genre, artists = artist)




"""
    Playlist According to Genres
"""
@app.route('/genre',methods=["GET","POST"])
def genre():
    songs = ['mood','sketches']
    return jsonify({'data': render_template("user_dashboard/genre.html",songs=songs)})




"""
    Playlist and Albums of Artists
"""
@app.route('/music/artist',methods=["GET","POST"])
def artist():
    music = []
    music.append(os.path.join("mood.mp3"))
    music.append(os.path.join("sketches.mp3"))
    return render_template("user_dashboard/music.html", songs=music)