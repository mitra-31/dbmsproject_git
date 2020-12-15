from app import app,mysql,bd,save_images,save_music
from flask import Flask,render_template,request,redirect,flash,session,url_for,current_app
from flask_fontawesome import fontawesome_css
from playsound import playsound
import os




@app.route('/dashboard',methods=["GET","POST"])
def dashboard():
    if request.method == "POST":
        title = request.form.get("title")
        data = save_music(request.files.get("data"))
        pic = save_images(request.files.get("pic"))
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO music.music(title,song,pic) VALUES(%s,%s,%s)",
                        (title,data,pic))
        mysql.connection.commit()
        cur.close()

    return render_template('user_dashboard/dashboard.html')
\
@app.route('/music',methods=["GET","POST"])
def music():
    cur = mysql.connection.cursor()
    cur.execute("select title,song,pic from music.music")
    music = cur.fetchall()
    print(music)
    #playsound("app\static\music\sketches.mp3")
    mysql.connection.commit()
    cur.close()
    return render_template("user_dashboard/music.html",music=set(music))


@app.route('/musicd',methods=["GET","POST"])
def mdashboard():
    return render_template("user_dashboard/music_dash.html")
    