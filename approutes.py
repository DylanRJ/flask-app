from flask import Blueprint


from flask import Blueprint, render_template

routes = Blueprint("routes", __name__)

@routes.route("/")
def homePage():
  return render_template("homepage.html")
