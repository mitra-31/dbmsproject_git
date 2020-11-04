from app import app,mysql
from app import dashboard
from flask import Flask,render_template,request,redirect,flash,session,url_for
from flask_fontawesome import fontawesome_css
import os


@app.route('/')
def home():
    home_img = os.path.join(app.config['UPLOAD_FOLDER'], 'band.png')
 
    return render_template('login/home.html',img1 = home_img)






## Login 
@app.route("/login",methods=['GET','POST'])
def login():
    login_img = os.path.join(app.config['UPLOAD_FOLDER'],'background.jpg')
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        cur = mysql.connection.cursor()
       
        cur.execute("SELECT username FROM logindetails WHERE username = '"+username+"'")
        usernamedata = cur.fetchone()
        passworddata = cur.execute("SELECT password FROM logindetails WHERE username = '"+username+"'")
        passworddata = cur.fetchone()
        mysql.connection.commit()
        cur.close()
        #print(usernamedata,passworddata)
        if usernamedata is None:
            flash("Username not found","danger")   
            return redirect(url_for("login"))

        if len(username) > 0 and len(password) > 0:
            if username in usernamedata and password in passworddata:
                flash("Login Successful","success")
                return redirect(url_for('dashboard'))
            else:
                flash(" Incorrect Password","danger")
                return redirect(url_for('login'))
        
    return render_template('login/signin.html' , img2 = login_img)



 ## register
@app.route("/register",methods=['GET','POST'])
def register():
    #to load background_iamge 
    login_img = os.path.join(app.config['UPLOAD_FOLDER'],'background.jpg')
    #inserting values inside loginDetials table
    if request.method == 'POST':
        user = request.form
        username = user['username']
        if username:
            flash("User Exists","danger")
            return redirect(url_for('register'))
        email = user['email']
        if email:
            flash("Email Exists Already","danger")
            return redirect(url_for("register"))
        password = user['password']
        confrim = user['confrim']
        
        if  len(username) > 0 and len(email) > 0 and len(password) > 0 and len(confrim) > 0:
            if password == confrim:
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO logindetails(username,email,password,confirm) VALUES(%s,%s,%s,%s)", ( username, email,  password, confrim))
                mysql.connection.commit()
                cur.close()
                flash("Successfully registered","success")                
                return redirect('/login')
            else:
                flash("password and confrim does not matched","danger")
                return redirect('/register')
        else:
            return "Enter everything"
        

    return render_template('login/signup.html' , img2 = login_img)



