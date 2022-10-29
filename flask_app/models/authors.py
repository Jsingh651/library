from flask_app.config.mysqlconnection import connectToMySQL

class Author:
    def __init__(self,data):
        self.id = data['id']
        self.author_name = data['author_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []

    @classmethod
    def get_all_authors (cls):
        query = 'SELECT * FROM authors'
        results = connectToMySQL('authors_books_schema').query_db(query)
        authors = []
        for i in results:
            authors.append(cls(i))
        return authors
    
    @classmethod
    def get_one_author (cls,data):
        query = 'SELECT * FROM authors WHERE id = %(id)s'
        results = connectToMySQL('authors_books_schema').query_db(query,data)
        return cls(results[0])

    @classmethod
    def create_author (cls, data):
        query = 'INSERT INTO authors(author_name) VALUES (%(author_name)s);'
        return connectToMySQL('authors_books_schema').query_db(query,data)