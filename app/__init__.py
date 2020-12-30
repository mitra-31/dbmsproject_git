from flask import Flask,current_app
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Bundle, Environment
from flask_mysqldb import MySQL
import os



app = Flask(__name__)




#images
imgfolder = os.path.join('static','img')
app.config['UPLOAD_FOLDER'] = imgfolder


#css Bundling
css = Bundle('css/home.css','css/signin.css','css/dashboard.css','css/profile.css','css/music_dash.css',output='gen/main.css')
assets = Environment(app)
assets.register('main_css',css)


def music(song):
    name = os.path.splitext(song.filename)
    print(os.path.splitext(song.filename))
    if name[1] in ".MP3,.mp3":
        title = name[0] + name[1]
    file_path = os.path.join(current_app.root_path, 'static/music',title)
    song.save(file_path)

    return title


"""
    To store mp3 files  in db and save mp3 file in given filepath
"""
def save_music(song):
    #print(song)
    name = os.path.splitext(song.filename)
    #print(os.path.splitext(song.filename))
    if name[1].lower() in ".mp3,.wav":
        music_name = name[0] + name[1]
    file_path = os.path.join(current_app.root_path, 'static/music',music_name)
    song.save(file_path)
    return music_name



"""
    To store images in db and save images in given filepath
"""
def save_images(photo):
    print(photo)
    name = os.path.splitext(photo.filename)
    print(os.path.splitext(photo.filename))
    if name[1].lower() in ".jpg,.png,.jpeg":
        photo_name = name[0] + name[1]
    file_path = os.path.join(current_app.root_path, 'static/img/uploads',photo_name)
    photo.save(file_path)
    return photo_name



"""
    Mysql Configurations 
"""
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'user123'
app.config['MYSQL_DB'] = 'project'
mysql = MySQL(app)





from app import login,dashboard