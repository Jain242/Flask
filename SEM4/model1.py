from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import enum 

db=SQLAlchemy()

class Gender(enum.Enum):
    male = 'муж'
    female = 'жен'

class Fags(db.Model):
    id_ = db.Column(db.Integer, primary_key = True)
    fag_name = db.Column(db.String(80), nullable = False)
    student = db.relationship('Students', backref=db.backref('fags'), lazy =True)
                    
    def __repr__(self) -> str:
        return f'Facult{self.id_} = {self.fag_name}'

class Students(db.Model):
    id_ = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(80), nullable = False)
    lastname = db.Column(db.String(80), nullable = False)
    age = db.Column(db.Integer, nullable = False)
    gender = db.Column(db.Enum(Gender), nullable = False)
    group = db.Column(db.Integer, unique = True, nullable = False)
    fags_id = db.Column(db.Integer, db.ForeignKey('fags.id_'),nullable = False)
    
    def __repr__(self) -> str:
        return f'Students({self.id_}, {self.firstname}, {self.lastname}, {self.age}, {self.gender}, {self.group})'
    

        

