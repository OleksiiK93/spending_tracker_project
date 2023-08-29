from db.run_sql import run_sql
from models.tag import Tag

def save(tag):
    sql = "INSERT INTO tags (name, deactivated) VALUES (%s, %s) RETURNING id"
    values = [tag.name, False]
    results = run_sql(sql, values)
    tag.id = results[0]['id']
    return tag

def select_all():
    tags = []
    sql = "SELECT * FROM tags ORDER BY name ASC"
    results = run_sql(sql)
    for row in results:
        tag = Tag(row['name'], row['deactivated'], row['id'])
        tags.append(tag)
    return tags

def select(id):
    tag = None
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        tag = Tag(result['name'], result['deactivated'], result['id'])
    return tag

def update(tag):
    sql = "UPDATE tags SET (name, deactivated) = (%s, %s) WHERE id = %s"
    values = [tag.name, tag.deactivated, tag.id]
    run_sql(sql, values)