from app import app, mysql, save_images
from app import dashboard
from flask import Flask, render_template, request, redirect, flash, session, url_for, current_app
from flask_fontawesome import fontawesome_css
import os

# home page


@app.route('/')
def home():
    slideImage1 = os.path.join(app.config['UPLOAD_FOLDER'], 'headphones.jpg')
    slideImage2 = os.path.join(app.config['UPLOAD_FOLDER'], 'band.png')
    slideImage3 = os.path.join(app.config['UPLOAD_FOLDER'], 'login.jpg')
    flask = os.path.join(app.config['UPLOAD_FOLDER'], 'flask.png')
    imagesOnWeb = [slideImage1, slideImage2, slideImage3, flask]
    return render_template('login/home.html', images=imagesOnWeb)


# Login
@app.route("/login", methods=['GET', 'POST'])
def login():
    login_img = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg')
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        cur = mysql.connection.cursor()

        cur.execute(
            "SELECT username FROM logindetails WHERE username = '"+username+"'")
        usernamedata = cur.fetchone()
        passworddata = cur.execute(
            "SELECT password FROM logindetails WHERE username = '"+username+"'")
        passworddata = cur.fetchone()
        mysql.connection.commit()
        cur.close()
        # print(usernamedata,passworddata)
        if usernamedata is None:
            flash("Username not found", "danger")
            return redirect(url_for("login"))

        if len(username) > 0 and len(password) > 0:
            if username in usernamedata and password in passworddata:
                flash("Login Successful", "success")
                return redirect(url_for('dashboard'))
            else:
                flash(" Incorrect Password", "danger")
                return redirect(url_for('login'))

    return render_template('login/signin.html', img2=login_img)

 # register


@app.route("/register", methods=['GET', 'POST'])
def register():
    # to load background_iamge
    login_img = os.path.join(app.config['UPLOAD_FOLDER'], 'background.jpg')
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

    return render_template('login/signup.html', img2=login_img)


@app.route("/profilepic", methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        photo = save_images(request.files.get('photo'))
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user(photo) VALUES(%s)", (photo))
        mysql.connection.commit()
        cur.close()
    return render_template("login/profilepic.html")
