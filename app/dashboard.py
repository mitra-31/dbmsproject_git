from app import app,mysql,bd
from flask import Flask,render_template,request,redirect,flash,session,url_for,current_app
from flask_fontawesome import fontawesome_css
import os




@app.route('/dashboard')
def dashboard():
        
    cur = mysql.connection.cursor()   
    cur.execute("SELECT * FROM user ")
    usersdetails = cur.fetchall()    
    return render_template('user_dashboard/dashboard.html',user=usersdetails)