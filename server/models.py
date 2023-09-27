from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Book(db.Model, SerializerMixin):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    authors = db.relationship('Author', backref='books')

    serialize_rules = ('-authors.books',)

class Author(db.Model, SerializerMixin):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))

    serialize_rules = ('-books.authors',)