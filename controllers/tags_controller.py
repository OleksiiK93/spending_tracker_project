from flask import Flask, render_template, request, redirect, Blueprint
import repositories.tag_repository as tag_repository
from models.tag import Tag

tags_blueprint = Blueprint("tags", __name__)

@tags_blueprint.route("/tags")
def tags():
    tags = tag_repository.select_all()
    sorted_tags = sorted(tags, key=lambda tag: tag.name.lower())
    return render_template("tags/index.html", tags = sorted_tags)

@tags_blueprint.route("/tags/new")
def new_tag():
    return render_template("tags/new.html")

@tags_blueprint.route("/tags", methods = ["POST"])
def create_tag():
    name = request.form['name']
    tag = Tag(name)
    tag_repository.save(tag)
    return redirect("/tags")

@tags_blueprint.route("/tags/<id>/edit")
def edit_tag(id):
    tag = tag_repository.select(id)
    return render_template("/tags/edit.html", tag = tag)

@tags_blueprint.route("/tags/<id>", methods = ["POST"])
def update_tag(id):
    tag = tag_repository.select(id)
    tag.name = request.form['name']
    if "deactivated" in request.form:
        tag.deactivate()
    else:
        tag.deactivated = False
    tag_repository.update(tag)
    return redirect("/tags")