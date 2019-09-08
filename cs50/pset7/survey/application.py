import csv

from flask import Flask, jsonify, redirect, render_template, request, url_for

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True
HOUSES = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
POSITIONS = ["Keeper", "Beater", "Chaser", "Seeker"]


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    # extract request form values
    name = request.form.get('name')
    house = request.form.get('house')
    position = request.form.get('position')

    # check validity
    if not name or not house or not position:
        return render_template("error.html", message="There are missing fields!")

    if len(name) < 2 or len(name) > 20:
        return render_template("error.html", message="The name must have between 2 and 20 chars!")

    if house not in HOUSES:
        return render_template("error.html", message="Invalid House selected!")

    if position not in POSITIONS:
        return render_template("error.html", message="Invalid Position selected!")

    # finally store the records
    if not store(name, house, position):
        return render_template("error.html", message="Could not save data!")

    # end redirect to the sheet overview
    return redirect(url_for('.get_sheet'))


@app.route("/sheet", methods=["GET"])
def get_sheet():
    rows = load()
    # explicit ask for is None, to not throw an error if the list is empty
    if rows is None:
        return render_template("error.html", message="Could not laod data")

    return render_template("sheet.html", rows=rows)


def load():
    """
    Load the csv or return none if an error occurs
    :return: the rows of the csv
    """
    try:
        with open('survey.csv', 'r') as f:
            reader = csv.reader(f)
            rows = list(reader)
    except Exception as e:
        print(f"Error {type(e).__name__} while loading data")
        return None
    return rows


def store(name, house, position):
    """
    try to store the data in a new row
    :return: true if success else false
    """
    try:
        with open("survey.csv", "a") as f:
            writer = csv.writer(f)
            writer.writerow((name, house, position))
            f.close()
    except Exception as e:
        print(f"Error {type(e).__name__} while storing data")
        return False

    return True
