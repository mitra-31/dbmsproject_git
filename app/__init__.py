from flask import Flask
from flask_assets import Bundle, Environment
from flask_mysqldb import MySQL
import os



app = Flask(__name__)

#images
imgfolder = os.path.join('static','img')
app.config['UPLOAD_FOLDER'] = imgfolder

#css Bundling
css = Bundle('css/home.css','css/signin.css','css/dashboard.css',output='gen/main.css')
assets = Environment(app)
assets.register('main_css',css)

#configure db

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root123'
app.config['MYSQL_DB'] = 'project'
mysql = MySQL(app)


from app import login