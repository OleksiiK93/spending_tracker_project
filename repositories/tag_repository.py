from db.run_sql import run_sql
from models.tag import Tag

def save(tag):
    sql = "INSERT INTO tags (name) VALUES (%s) RETURNING id"
    values = [tag.name]
    results = run_sql(sql, values)
    tag.id = results[0]['id']
    return tag

def select_all():
    tags = []
    sql = "SELECT * FROM tags"
    results = run_sql(sql)
    for row in results:
        tag = Tag(row['name'], row['id'])
        tags.append(tag)
    return tags

def select(id):
    tag = None
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        tag = Tag(result['name'], result['id'])
    return tag

def update(tag):
    sql = "UPDATE tags SET name = %s WHERE id = %s"
    values = [tag.name, tag.id]
    run_sql(sql, values)