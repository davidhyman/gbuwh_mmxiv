This file to contain instructions for developing the project.

The project is in Python/Django
https://docs.djangoproject.com/en/1.6/

You'll need to get python. I was using 2.7 but if you have strong opinions we can go with 3
https://www.python.org/downloads/

Use good coding style:
http://legacy.python.org/dev/peps/pep-0008/

I use virtual environments to ensure stuff doesn't get messed up:
https://pypi.python.org/pypi/virtualenv
on windows:
pip install virtualenvwrapper-win
mkvirtualenv <project name>
workon <project name>

install the requirements:
pip install -r requirements.txt

you can run the project dev server with:
python manage.py runserver

more docs on the web, or get in touch