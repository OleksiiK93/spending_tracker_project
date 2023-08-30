from flask import Flask, render_template, request, redirect, Blueprint
import repositories.budget_repository as budget_repository
from models.budget import Budget
import pdb

budgets_blueprint = Blueprint("budgets", __name__)

@budgets_blueprint.route("/budgets", methods = ["POST"])
def create_budget():
    amount = request.form['amount']
    # pdb.set_trace()
    budget = Budget(amount)
    budget_repository.save(budget)
    return redirect("/transactions")

@budgets_blueprint.route("/budgets/delete", methods = ["POST"])
def delete_all():
    budget_repository.delete_all()
    return redirect("/transactions")