# 🦸 Superheroes API

This is a RESTful API for managing superheroes, their powers, and the strengths of each power per hero.

## 🔗 Base URL

http://127.0.0.1:5000


## 📦 Technologies Used

- Python 3.8+
- Flask
- SQLAlchemy
- Flask-Migrate
- SQLite (development)

## 🛠️ Setup Instructions

1. Clone the repo:
git clone git@github.com:4512yasir/superHeroe_api.git
cd superheroes-api

## Create a virtual environment:
python3 -m venv venv
source venv/bin/activate
## Install dependencies:
pip install -r requirements.txt
## Initialize database:
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
## Seed data
python seed.py
## Run the server:
flask run

# created by  
Mercy owino