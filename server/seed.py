from random import sample, randint, choice
from faker import Faker
from models import db, Book, Author
from app import app

book_titles = [
    "Whispers of the Heart",
    "Echoes in the Night",
    "Fragments of Love",
    "Secrets of the Past",
    "Tears of Redemption",
    "Sins of the Soul",
    "Promises Kept",
    "Shadows of Deception",
    "Lost in Love's Embrace",
    "Dancing with Fate",
    "The Healing Touch",
    "Beneath the Moonlight",
    "In Search of Tomorrow",
    "Forgotten Dreams",
    "A Love Beyond Time",
    "Eternal Whispers",
    "Whispers from the Past",
    "Passion's Promise",
    "Midnight Serenade",
    "Enchanted Hearts",
]



fake = Faker()

# Clear existing data
with app.app_context():
    Book.query.delete()
    Author.query.delete()

    # Create books and authors
    books = []
    authors = []

    unique_titles = sample(book_titles, 20)  # Sample 20 unique titles from the list

    for title in unique_titles:
        book = Book(
            name=title,
        )
        books.append(book)

    for _ in range(10):
        author = Author(
            name=fake.name(),
            book_id = randint(1, len(books)),
        )
        authors.append(author)

    # Add books and authors to the database
    db.session.add_all(books)
    db.session.add_all(authors)
    db.session.commit()
