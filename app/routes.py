from app import app, db
from app.models import User 
from flask import render_template, jsonify, request, redirect
from flask_cors import CORS, cross_origin


@app.route('/', methods = ["GET", "POST"])
def index():
    showHtml = {"form": 1, "new_draw": 0}

    if request.method == "POST":
        username = request.form["username"]
        country = request.form["country"]
        color = request.form["color"]
        try:
            register = User(username=username, country=country, color=color)
            db.session.add(register)
            db.session.commit()

            showHtml = {"form": 0, "new_draw": 1}

            showHtml["username"] = username
            showHtml["country"] = country
            showHtml["color"] = color

            
            print("New draw", register.__repr__())
            print("Saved!\n")
            return render_template("base.html", showHtml=showHtml)


        except Exception as e:
            showHtml["error"] = str(e)
            print("No saved! bacause:\n", e)


    return render_template("base.html", showHtml=showHtml)


@app.get('/all_users')
def getAll_users():
    showHtml = {"form": 1, "show_users": 0}

    try:
        all_users = User.query.all()
        showHtml = {"form": 0, "show_users": 1}
        if not all_users:
            showHtml["error"] = "There are empty users."
            return render_template("base.html", showHtml=showHtml)

        showHtml["table"] = 1
        return render_template("base.html", showHtml=showHtml, users=all_users)

    except Exception as e:
        showHtml["error"] = str(e)
    
    return render_template("base.html", showHtml=showHtml)