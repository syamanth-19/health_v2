from flask import Flask
from flask_login import LoginManager
from dotenv import load_dotenv
import os
from models import db 


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

import mainrouter1 
app.register_blueprint(mainrouter1.mr)
login_manager = LoginManager() # create login controller
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mh.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to reduce mem usage, helps for debugging 
login_manager.init_app(app)
login_manager.login_view = 'mainrouter.login'
db.init_app(app)

from models import mhusers

@login_manager.user_loader
def load_user(user_id):
    try: 
        return db.session.execute(db.select(mhusers).filter_by(id=user_id)).scalar_one_or_none()
    except: 
        return None  
    
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port = 7890)