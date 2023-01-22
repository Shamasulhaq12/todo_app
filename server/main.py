"""starting point of the project in flask."""
from app import app, db

if __name__ == '__main__':

    db.create_all()
    app.run()
