from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
auth =HTTPBasicAuth()

app.app_context().push()
from .routes import api
db.create_all()
db.session.commit()

if __name__ == '__main__':

    
    app.run()
