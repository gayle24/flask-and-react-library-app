from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Resource, Api
from models import db, Book, Author

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///book_authors.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

@app.route('/')
def home():
    return {"hello": "Welcome to my api"}

class Books(Resource):
    def get(self):
        books = Book.query.all()
        response_dict_list = []
        # response_dict = book.to_dict()
        for item in books:
            response_dict = {
                "title": item.name,
                "id": item.id,
                # "author": item.authors,
            }
            response_dict_list.append(response_dict)
        response = make_response(
            jsonify(response_dict_list),
            200
        )
        return response
api.add_resource(Books, '/books')

@app.route('/authors')
def authors():
    pass
    response_dict_list = [item.to_dict() for item in Author.query.all()]
    response = make_response(
        jsonify(response_dict_list),
        200
    )
    return response

if __name__ == '__main__':
    app.run()