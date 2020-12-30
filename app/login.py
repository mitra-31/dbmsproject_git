from app import app, mysql, save_images
from app import dashboard
from flask import Flask, render_template, request, redirect, flash, session, url_for, current_app
from flask_fontawesome import fontawesome_css
import os


# Home page

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index/home.html')


# User Login

@app.route("/user/login", methods=['GET', 'POST'])
def user_login():
   
    if request.method == "POST":
        """
            Retriving data from html forms
        """
        username = request.form.get("username") 
        password = request.form.get("password")

        """
            Retriving data from database and validating html form and database
        """
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT username FROM logindetails WHERE username = '{0}'".format(username))
        usernamedata = cur.fetchone()
        cur.execute(
            "SELECT password FROM logindetails WHERE username = '{0}'".format(username))
        passworddata = cur.fetchone()
        mysql.connection.commit()
        cur.close()


        # Validation 
        if usernamedata is None:
            return redirect(url_for("login"))

        if len(username) > 0 and len(password) > 0:
            if username in usernamedata and password in passworddata:
                return redirect(url_for('home'))
            else:
                return redirect(url_for('login'))

    return render_template('index/signin.html')


# User Register

@app.route("/user/register", methods=['GET', 'POST'])
def user_register():

    if request.method == 'POST':
        """
            Retriving data from User registerations form
        """
        user = request.form
        firstname = user['firstname']
        lastname = user['lastname']
        email = user['email']
        password = user['password']

        """
            Connecting to database and Inserting data into table
        """
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user(firstname,lastname,email,password) VALUES(%s,%s,%s,%s)",
                    (firstname, lastname, email, password))
        mysql.connection.commit()
        cur.close()
        return redirect('music')

    return render_template('index/signup.html')


# Admin Login

@app.route("/user/login", methods=['GET', 'POST'])
def admin_login():

    if request.method == "POST":
        """
            Retriving data from html forms
        """
        username = request.form.get("username") 
        password = request.form.get("password")

        """
            Retriving data from database and validating html form and database
        """
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT username FROM logindetails WHERE username = '{0}'".format(username))
        usernamedata = cur.fetchone()
        cur.execute(
            "SELECT password FROM logindetails WHERE username = '{0}'".format(username))
        passworddata = cur.fetchone()
        mysql.connection.commit()
        cur.close()

        #Validation 

        if usernamedata is None:
            return redirect(url_for("login"))

        if len(username) > 0 and len(password) > 0:
            if username in usernamedata and password in passworddata:
                return redirect(url_for('home'))
            else:
                flash(" Incorrect Password", "danger")
                return redirect(url_for('login'))

    return render_template('index/signin.html')


# admin registrations

@app.route("/user/register", methods=['GET', 'POST'])
def admin_register():
    if request.method == 'POST':
        admin = request.form
        firstname = admin['firstname']
        lastname = admin['lastname']
        email = admin['email']
        password = admin['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user(firstname,lastname,email,password) VALUES(%s,%s,%s,%s)",
                    (firstname, lastname, email, password))
        mysql.connection.commit()
        cur.close()
        return redirect('/admin/login')

    return render_template('index/signup.html')
