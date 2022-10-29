from flask_app import app
from flask import Flask, redirect, request, render_template
from flask_app.models.authors import Author
from flask_app.models.books import Book

@app.route('/books/add')
def viewpage():
    all_books = Book.get_all_books()
    return render_template('books.html',all_books = all_books)

@app.route('/add/update',methods = ['POST'])
def addbook():
    data = {
        'book_name': request.form['book_name'],
        'pages': request.form['pages']
    }
    Book.create_book(data)
    return redirect('/books/add')