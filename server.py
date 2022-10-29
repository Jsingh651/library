from flask_app import app
from flask_app.controllers import authorsController 
from flask_app.controllers import booksController

if __name__ == '__main__':
    app.run(debug = True, port = 3001)