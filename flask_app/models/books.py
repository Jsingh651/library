from flask_app.config.mysqlconnection import connectToMySQL

class Book:
    def __init__(self,data):
        self.id = data['id']
        self.book_name = data['book_name']
        self.pages = data['pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors = []

    @classmethod
    def get_all_books(cls):
        query = 'SELECT * FROM books'
        results = connectToMySQL('authors_books_schema').query_db(query)
        books = []
        for i in results:
            books.append(cls(i))
        return books
    
    @classmethod
    def get_one_book (cls,data):
        query = 'SELECT * FROM books WHERE id = %(id)s'
        results = connectToMySQL('authors_books_schema').query_db(query,data)
        return cls(results[0])

    @classmethod
    def create_book (cls, data):
        query = 'INSERT INTO books (book_name, pages) VALUES (%(book_name)s, %(pages)s);'
        return connectToMySQL('authors_books_schema').query_db(query,data)


    @classmethod
    def get_books_with_authors(cls,data):


# @classmethod
# def get_topping_with_burgers( cls , data ):
#     query = "SELECT * FROM toppings LEFT JOIN add_ons ON add_ons.topping_id = toppings.id LEFT JOIN burgers ON add_ons.burger_id = burgers.id WHERE toppings.id = %(id)s;"
#     results = connectToMySQL('burgers').query_db( query , data )
#         # results will be a list of topping objects with the burger attached to each row. 
#     topping = cls( results[0] )
#     for row_from_db in results:
#             # Now we parse the topping data to make instances of toppings and add them into our list.
#            burger_data = {
#                "id" : row_from_db["burgers.id"],
#                "name" : row_from_db["name"],
#                "bun" : row_from_db["bun"],
#                "calories" : row_from_db["calories"],
#                "created_at" : row_from_db["toppings.created_at"],
#                "updated_at" : row_from_db["toppings.updated_at"]
#            }
#            topping.on_burgers.append( burger.Burger( burger_data ) )
#        return topping