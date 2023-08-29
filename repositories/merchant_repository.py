from db.run_sql import run_sql
from models.merchant import Merchant

def save(merchant):
    sql = "INSERT INTO merchants (name, deactivated) VALUES (%s, %s) RETURNING id"
    values = [merchant.name, False]
    results = run_sql(sql, values)
    merchant.id = results[0]['id']
    return merchant

def select_all():
    merchants = []
    sql = "SELECT * FROM merchants ORDER BY name ASC"
    results = run_sql(sql)
    for row in results:
        merchant = Merchant(row['name'], row['deactivated'], row['id'])
        merchants.append(merchant)
    return merchants

def select(id):
    merchant = None
    sql = "SELECT * FROM merchants WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        merchant = Merchant(result['name'], result['deactivated'], result['id'])
    return merchant

def update(merchant):
    sql = "UPDATE merchants SET (name, deactivated) = (%s, %s) WHERE id = %s"
    values = [merchant.name, merchant.deactivated, merchant.id]
    run_sql(sql, values)