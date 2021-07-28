If you just want to clone the project and get it up running, below is how to do:
Clone git:
o	git clone  
Cd into it:
o	cd sumiasell
	Create a venv:
o	python3 -m venv venv
	Activate venv:
o	On Mac/Linux: source venv/bin/activate
o	On Windows: venv\Scripts\activate
	Install the requirements:
o	pip install -r requirements.txt
Create DB
o	python manage.py makemigrations
	Apply DB Changes:
o	python manage.py migrate
	Run the server:
o	python manage.py runserver
Navigate to the site: http://127.0.0.1:8000
Follow the instructions on the about page to start using the site
