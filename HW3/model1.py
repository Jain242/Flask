from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Author(db.Model):
    id_ = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    lastname = db.Column(db.String(80), nullable = False)
                    
    def __repr__(self) -> str:
        return f'Facult{self.id_} {self.name}{self.lastname}'

class Books(db.Model):
    id_ = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    years_start = db.Column(db.Integer, nullable=False)
    copies  = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id_'),nullable = False)
    author = db.relationship('Author', backref='books')
    
    def __repr__(self) -> str:
        return f'Books({self.id_}, {self.name}, {self.years_start}, {self.copies }, {self.author_id}, )'
    

        

