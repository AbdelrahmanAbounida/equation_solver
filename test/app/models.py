from datetime import datetime
from .extensions import db
from app import login_manager
from flask_login import UserMixin

class User(db.Model,UserMixin):
    __tablename__ = 'User'
    # __table_args__ = {'extend_existing': True}
    
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(50),unique=True,nullable=False)
    password = db.Column(db.String(10),nullable=False)

    def __repr__(self) -> str:
        return f"User: {self.email.split('@')[0]}"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


## create db
# from app import app
# from app.models import User, Task
# with app.app_context():
#     db.create_all()
# with app.app_context()::
#   db.session.add(user)


## delete database 
# db.session.query(User).delete()