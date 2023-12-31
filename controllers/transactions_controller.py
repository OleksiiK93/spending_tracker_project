from flask import Flask, render_template, request, redirect, Blueprint
import repositories.transaction_repository as transaction_repository
import repositories.merchant_repository as merchant_repository
import repositories.tag_repository as tag_repository
import repositories.budget_repository as budget_repository
from models.transaction import Transaction

transactions_blueprint = Blueprint("transactions", __name__)

@transactions_blueprint.route("/transactions")
def transactions():
    transactions = transaction_repository.select_all()
    total = transaction_repository.total()
    budget = None
    balance = None
    debt = None
    budgets = budget_repository.select_all()
    if len(budgets) > 0:
        budget = budgets[-1]
        balance = budget.amount - total
        debt = abs(balance)       
    return render_template("transactions/index.html", transactions = transactions, total = total, budget = budget, balance = balance, debt = debt)

@transactions_blueprint.route("/transactions/new")
def new_transaction():
    merchants = merchant_repository.select_all()
    tags = tag_repository.select_all()
    return render_template("transactions/new.html", merchants = merchants, tags = tags)

@transactions_blueprint.route("/transactions", methods = ["POST"])
def create_transaction():
    amount = request.form['amount']
    merchant_id = request.form['merchant_id']
    tag_id = request.form['tag_id']
    timestamp = request.form['date_time']
    merchant = merchant_repository.select(merchant_id)
    tag = tag_repository.select(tag_id)
    transaction = Transaction(merchant, tag, amount, timestamp)
    transaction_repository.save(transaction)
    return redirect("/transactions")

@transactions_blueprint.route("/transactions/<id>/delete", methods=['POST'])
def delete_transaction(id):
    transaction_repository.delete(id)
    return redirect('/transactions')