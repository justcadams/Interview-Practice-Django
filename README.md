### Welcome to my branch exploring Django, Djongo, MongoDB, React, and Python!

#### If you don't have Python3 please follow this link:

https://www.python.org/downloads/

#### If you don't Pip please follow this link:

https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

I recommend creating a \<Project\> folder to work within.
I named my folder Django.


1. Open a command prompt or terminal and navigate to your \<Project\> folder.


2. Git clone this repository https://github.com/justcadams/Interview-Practice-Django.git.


3. Create a .env file in the \<Project\> folder.


4. Fill out the .env as the example.env file demonstrates.


5. Create a virtual environment:

	5a. Install a virtual environment library using pip:

		python3 -m pip install --user virtualenv

	5b. Create a local virtual environment:

		python3 -m venv env

	5c. Activate the local virtual environment:

		On macOS and Linux: source env/bin/activate
		On Windows: .\env\Scripts\activate


6. Install all the requirements with the following command:

		python3 -m pip install -r requirements.txt


7. Open the mysite directory in your command prompt or terminal.


8. Enter the following command to start the service:

		python3 manage.py runserver
	Note: This will run on port 8000 by default.
	
	(Make sure no other application is using this port when you run this command).


9. You can change the port the Django server runs on by specifying it as follows:

		python3 manage.py runserver 127.0.0.1:5000