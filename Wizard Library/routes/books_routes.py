from flask import Blueprint

import controllers

books = Blueprint('books', __name__)

@books.route('/book', methods=['POST'])
def add_book():
    return controllers.books_controller.add_book()

@books.route('/books', methods=['GET'])
def get_books():
    return controllers.books_controller.get_books()

@books.route('/book/available', methods=['GET'])
def get_available_books():
    return controllers.books_controller.get_available_books()

@books.route('/book/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    return controllers.books_controller.update_book(book_id)

@books.route('/book/delete/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    return controllers.books_controller.delete_book(book_id)
