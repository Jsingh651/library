from flask_app import app
from flask import Flask, redirect, request, render_template
from flask_app.models.authors import Author

@app.route('/')
def show ():
    getall = Author.get_all_authors()
    return render_template('authors.html',getall = getall)

@app.route('/author/show', methods = ['POST'])
def addauthor ():
    data = {
        'author_name': request.form['author_name']
    }
    Author.create_author(data)
    return redirect ('/')