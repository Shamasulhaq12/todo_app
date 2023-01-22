"""starting point of the project in flask."""
from app import app, db

if __name__ == '__main__':
#This function is called when the file is run directly and created all the tables in the database.
    db.create_all()
    app.run()
