from flask import Flask, request, jsonify

from db import db
from models.books import Books

def add_book():
    post_data = request.form if request.form else request.json
    fields = ["title", "author", "genre", "published_year", "active"]
    required_fields = ["title", "author"]

    values = {}

    for field in fields:
        field_data = post_data.get(field)
        if field in required_fields and not field_data:
            return jsonify({'message': f'Missing required field: {field}'}), 400
        values[field] = field_data
        
    new_book = Books(
        title=values.get("title"),
        author=values.get("author"),
        genre=values.get('genre'),
        published_year=values.get('published_year'),
        active=values.get('active', True))
    
    try:
        db.session.add(new_book)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error adding book: {str(e)}'}), 500
    
    query = db.session.query(Books).filter(Books.title == values["title"]).first()
    book = {
        "book_id": str(query.book_id),
        "title": query.title,
        "author": query.author,
        "genre": query.genre,
        "published_year": query.published_year,
        "active": query.active
    }
    return jsonify({'message': 'Book added successfully!', "result": book}), 201

def get_books():

    query = db.session.query(Books).all()
    if not query:
        return jsonify({'message': 'No books found.'}), 404 
    books = []
    for book in query:
        books.append({
            "book_id": str(book.book_id),
            "title": book.title,
            "author": book.author,
            "genre": book.genre,
            "published_year": book.published_year,
            "active": book.active
        })
    return jsonify({'message': 'Books retrieved successfully!', "books": books}), 200

def get_available_books():
    query = db.session.query(Books).filter(Books.active == True).all()
    if not query:
        return jsonify({'message': 'No available books found.'}), 404
    books = []
    for book in query:
        books.append({
            "book_id": str(book.book_id),
            "title": book.title,
            "author": book.author,
            "genre": book.genre,
            "published_year": book.published_year,
            "active": book.active
        })
    return jsonify({'message': 'Available books retrieved successfully!', "books": books}), 200

def update_book(book_id):
    post_data = request.form if request.form else request.json
    fields = ["title", "author", "genre", "published_year", "active"]
    values = {}

    for field in fields:
        field_data = post_data.get(field)
        if field_data is not None:
            values[field] = field_data

    query = db.session.query(Books).filter(Books.book_id == book_id).first()
    if not query:
        return jsonify({'message': 'Book not found.'}), 404

    for key, value in values.items():
        setattr(query, key, value)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error updating book: {str(e)}'}), 500

    book = {
        "book_id": str(query.book_id),
        "title": query.title,
        "author": query.author,
        "genre": query.genre,
        "published_year": query.published_year,
        "active": query.active
    }
    return jsonify({'message': 'Book updated successfully!', "result": book}), 200

def delete_book(book_id):
    query = db.session.query(Books).filter(Books.book_id == book_id).first()
    if not query:
        return jsonify({'message': 'Book not found.'}), 404

    try:
        db.session.delete(query)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'Error deleting book: {str(e)}'}), 500

    return jsonify({'message': 'Book deleted successfully!'}), 200