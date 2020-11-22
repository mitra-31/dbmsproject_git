#To run this project follow these steps

STEP 1 

-> Unziping the file after downloading 

****************************************************************

STEP 2

-> Creating a virtual environment for this project

-> open the download folder in command prompt 

	( Example: if your unzipped folder is in downloads cmd: cd Downloads\music-app-flask)

-> After you moving to project directory type this cmd:
			
	pip install virtualenv        //to install virtual environment


-> Soon after packages get download type this cmd: 

	virtualenv (name your virtual env)   [example: virtualenv base]    //to create virtual environment

-> Now, move to your virtual environment by following cmd: 

	(name your virtual env)\Scripts\activate  [example: base\Scripts\activate]

***********************************************************************************************************************************

STEP 3

-> Downloading Flask packages to run the project

-> To download flask use this cmd:

	pip install -r requirements.txt

-> If you get Error for above cmd install flask manaully

	pip install flask flask-assets flask-fontawesome flask-MySQLdb

*******************************************************************************************************

#How to run the project

-> Its simple to run the project
	
	first you have to be in your virtual environment [example: (env) cd:\ User\username\download\music-app-flask]
	
	cmd: py run.py

-> after cmd runs sucessfully open your browser and search for this :
	
	http://127.0.0.1:5000/
