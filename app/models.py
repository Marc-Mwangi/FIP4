from enum import unique
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

class User(UserMixin,db.Model):

    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), index= True)
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    quote= db.relationship('Quote', backref='user', lazy="dynamic")
    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
            self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

    
    from . import login_manager

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    
    def __repr__(self):
        return f'User{self.username}'
class Quote(db.Model):
        __tablename__= 'post'
        id = db.Column(db.Integer, primary_key = True)
        quote = db.Column(db.String(255),unique = True,index = True)
        user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
        
                
        def __repr__(self):
                return f'User{self.quote}'
        
class Comment(db.Model):
        __tablename__= 'comment'
        id = db.Column(db.Integer, primary_key = True)
        q_comment = db.Column(db.String(255),unique = True,index = True)
        
