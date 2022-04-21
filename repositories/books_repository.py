from db.run_sql import run_sql

from models.books import Books
from models.authors import Authors
import repositories.authors_repository as authors_repository

def save(books):
    sql = "INSERT INTO books (title, authors_id) VALUES (%s, %s) RETURNING *"
    values = [books.title, books.authors.id] 
    results = run_sql(sql, values)
    id = results[0]['id']
    books.id = id
    return books

def delete_all():
    sql = "DELETE  FROM books"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)