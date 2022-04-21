import pdb
from models.books import Books
from models.authors import Authors

import repositories.books_repository as books_repository
import repositories.authors_repository as authors_repository

authors_repository.delete_all()
books_repository.delete_all()

author1 = Authors("John", "Johnson")
authors_repository.save(author1)

book1 = Books("John's book", author1)
books_repository.save(book1)