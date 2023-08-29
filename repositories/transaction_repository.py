from db.run_sql import run_sql
from models.transaction import Transaction
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository

def save(transaction):
    sql = "INSERT INTO transactions (merchant_id, tag_id, amount, timestamp) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [transaction.merchant.id, transaction.tag.id, transaction.amount, transaction.timestamp]
    results = run_sql(sql, values)
    id = results[0]['id']
    transaction.id = id
    return transaction

def select_all():
    transactions = []
    sql = "SELECT * FROM transactions ORDER BY timestamp DESC"
    results = run_sql(sql)
    for row in results:
        merchant = merchant_repository.select(row['merchant_id'])
        tag = tag_repository.select(row['tag_id'])
        transaction = Transaction(merchant, tag, row['amount'], row['timestamp'], row['id'])
        transactions.append(transaction)
    return transactions

def total():
    total = 0
    sql = "SELECT amount FROM transactions"
    results = run_sql(sql)
    for row in results:
        amount = row['amount']
        total += amount
    return total

