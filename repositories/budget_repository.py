from db.run_sql import run_sql
from models.budget import Budget
import pdb

def save(budget):
    sql = "INSERT INTO budgets (amount) VALUES (%s) RETURNING id"
    values = [budget.amount]
    # pdb.set_trace()
    results = run_sql(sql, values)
    budget.id = results[0]['id']
    return budget

def select_all():
    budgets = []
    sql = "SELECT * FROM budgets"
    results = run_sql(sql)
    for row in results:
        budget = Budget(row['amount'], row['id'])
        budgets.append(budget)
    return budgets

def delete_all():
    sql = "DELETE FROM budgets"
    run_sql(sql)