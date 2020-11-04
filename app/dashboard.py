from app import app,mysql
from flask import Flask,render_template,request,redirect,flash,session,url_for
from flask_fontawesome import fontawesome_css
import os


@app.route('/dashboard')
def dashboard():
    home_img1 = os.path.join(app.config['UPLOAD_FOLDER'], 'band.png')
    home_img2 = os.path.join(app.config['UPLOAD_FOLDER'], 'bg.jpg')
    home_img3 = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg')
    
    return render_template('user_dashboard/dashboard.html',img1 = home_img1 , img2 = home_img2, img3 = home_img3)