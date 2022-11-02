# Fyyur

## Introduction

Fyyur is a musical venue and artist booking site that facilitates the discovery and bookings of shows between local performing artists and venues. This site lets you list new artists and venues, discover them, and list shows with artists as a venue owner.
This project is part of the assemment for a Full-stack web developer course at Udacity, sponsored by [Alx-T](https://www.alx-t.com/).

## Tech Stack
- virtualenv as a tool to create isolated Python environments
- SQLAlchemy ORM to be our ORM library of choice
- PostgreSQL as our database of choice
- Python3 and Flask as our server language and server framework
- Flask-Migrate for creating and running schema migrations.
- HTML, CSS, and Javascript with Boostrap 3 for the website.

## File Structure
```sh
    ├── README.md
    ├── app.py *** the main driver of the app. 
    ├── config.py *** Database URLs, CSRF generation, etc
    ├── error.log
    ├── forms.py
    ├── models.py
    ├── requirements.txt 
    ├── static
    │   ├── css 
    │   ├── font
    │   ├── ico
    │   ├── img
    │   └── js
    └── templates
        ├── errors
        ├── forms
        ├── layouts
        └── pages
```
 ## How to Launch
 1. Install the depencies into your virtual enviroment using 
      `pip install -r requirements.txt`
 2. The app would run with Postgres database. You can install postgressql form [here](https://www.postgresqltutorial.com/postgresql-python/connect/).
 3. Create a database for the app `flyyurdb`. Or choose a new name for your database but you would have to edit the database URI in `config.py.`
 4. create the database from the app.py using `flask db migrate`. And update the content of the database `flask db upgrade`.
 5. Run the app `flask run`.
 


