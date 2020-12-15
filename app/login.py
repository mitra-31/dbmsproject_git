from app import app, mysql, save_images
from app import dashboard
from flask import Flask, render_template, request, redirect, flash, session, url_for, current_app
from flask_fontawesome import fontawesome_css
import os






"""
    Intro page of the webiste where user or musican can login or signup

"""
@app.route('/' , methods=['GET','POST'])
def home():
    flash("Login Successful", "success")
    slideImage1 = os.path.join(app.config['UPLOAD_FOLDER'], 'headphones.jpg')
    slideImage2 = os.path.join(app.config['UPLOAD_FOLDER'], 'band.png')
    slideImage3 = os.path.join(app.config['UPLOAD_FOLDER'], 'login.jpg')
    flask = os.path.join(app.config['UPLOAD_FOLDER'], 'flask.png')
    imagesOnWeb = [slideImage1, slideImage2, slideImage3, flask]
    return render_template('index/home.html', images=imagesOnWeb)


"""
    Login validation will be done using this function

"""


@app.route("/login", methods=['GET', 'POST'])
def login():
    dummy = os.path.join(app.config['UPLOAD_FOLDER'], 'dummy.png')

    if request.method == "POST":
        username = request.form.get("username")
        print(username)
        password = request.form.get("password")
        cur = mysql.connection.cursor()
        cur.execute("SELECT username FROM logindetails WHERE username = '{0}'".format(username))
        usernamedata = cur.fetchone()
        cur.execute("SELECT password FROM logindetails WHERE username = '{0}'".format(username))
        passworddata = cur.fetchone()
        mysql.connection.commit()
        cur.close()
        # print(usernamedata,passworddata)
        if usernamedata is None:
            flash("Username not found", "danger")
            return redirect(url_for("login"))

        if len(username) > 0 and len(password) > 0:
            if username in usernamedata and password in passworddata:
                return redirect(url_for('home'))
            else:
                flash(" Incorrect Password", "danger")
                return redirect(url_for('login'))

    return render_template('index/signin.html', dummy=dummy)

 # register
@app.route("/register", methods=['GET', 'POST'])
def register():
    # to load background_iamge
    dummy = os.path.join(app.config['UPLOAD_FOLDER'], 'dummy.png')

    # inserting values inside loginDetials table
    if request.method == 'POST':
        user = request.form
        firstname = user['firstname']
        lastname = user['lastname']
        email = user['email']
        password = user['password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user(firstname,lastname,email,password) VALUES(%s,%s,%s,%s)",
                    (firstname, lastname, email, password))
        mysql.connection.commit()
        cur.close()
        flash("Successfully registered", "success")
        return redirect('/profilepic')
    return render_template('index/signup.html',  dummy=dummy)


