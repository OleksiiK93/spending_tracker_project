from flask import Flask, render_template, request, redirect, Blueprint
import repositories.merchant_repository as merchant_repository
from models.merchant import Merchant

merchants_blueprint = Blueprint("merchants", __name__)

@merchants_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all()
    sorted_merchants = sorted(merchants, key=lambda merchant: merchant.name.lower())
    return render_template("merchants/index.html", merchants = sorted_merchants)

@merchants_blueprint.route("/merchants/new")
def new_merchant():
    return render_template("merchants/new.html")

@merchants_blueprint.route("/merchants", methods = ["POST"])
def create_merchant():
    name = request.form['name']
    merchant = Merchant(name)
    merchant_repository.save(merchant)
    return redirect("/merchants")

@merchants_blueprint.route("/merchants/<id>/edit")
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template("/merchants/edit.html", merchant = merchant)

@merchants_blueprint.route("/merchants/<id>", methods = ["POST"])
def update_merchant(id):
    merchant = merchant_repository.select(id)
    merchant.name = request.form['name']
    if "deactivated" in request.form:
        merchant.deactivate()
    else:
        merchant.deactivated = False
    merchant_repository.update(merchant)
    return redirect("/merchants")