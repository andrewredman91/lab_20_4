from db.run_sql import run_sql

from models.authors import Authors
from models.books import Books

def save(authors):
    sql = "INSERT INTO authors (first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [authors.first_name, authors.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    authors.id = id
    return authors

def delete_all():
    sql = "DELETE  FROM authors"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM users WHERE id = %s"
    values = [id]
    run_sql(sql, values)