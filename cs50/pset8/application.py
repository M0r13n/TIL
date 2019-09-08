import os

from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# needs to be placed here to prevent a deprecation warning
from db import *

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    uid = session.get("user_id")
    if uid is None:
        return apology("Invalid request, please login again")

    stocks = query_stock(uid)
    cash = total = get_user_by_id(uid)[0]['cash']

    # This is blocking and therefore blocks page rendering --> Could be done asynchronously  or fetched after page load in background
    for stock in stocks:
        res = lookup(stock["symbol"])
        shares = stock["shares"]
        stock["name"] = res["name"]
        stock["price"] = usd(res["price"])
        stock["total"] = usd(res["price"] * shares)
        total += res["price"] * shares

    return render_template("index.html", stocks=stocks, cash=usd(cash), total=usd(total))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "POST":

        # Form validation
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        uid = session.get("user_id")

        if None in (symbol, shares, uid):
            return apology("Invalid request")

        # Get necessary data
        res = lookup(symbol)
        if res is None:
            return apology("Could not lookup data")

        name, price, symbol = res.values()

        # Check users credit balance
        cash = get_user_by_id(uid)
        if cash is None or len(cash) == 0:
            return apology("Could not lookup data")

        cash = cash[0]["cash"]

        new_cash = cash - price * shares

        if new_cash < 0:
            return apology("You are broke, dude")

        # ATTENTION - NOT SAFE: If the first operation succeeds and the second fails,
        # the database will get corrupted!
        #
        # How to fix: Use some framework like sqlalchemy, to be able to rollback transactions
        # or commit after both operations succeed
        if False in (update_user_cash(uid, new_cash), add_transaction(uid, symbol, shares, price), add_stock(uid, symbol, shares)):
            return apology("Could not process transaction")

        return redirect("/")

    return render_template("buy.html")


@app.route("/check", methods=["GET"])
def check():
    """Return true if username available, else false, in JSON format"""
    return jsonify("TODO")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    if request.method == "POST":
        symbol = request.form.get("symbol")

        if symbol is None:
            return apology("Invalid request")

        result = lookup(symbol)

        if result is None:
            return apology("Could not lookup data")

        return render_template("quoted.html", name=result["name"], symbol=result["symbol"], price=usd(result["price"]))

    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        # Check form data is valid
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if None in (username, password, confirmation):
            return apology("Incomplete Data", 400)

        if len(username) < 1:
            return apology("Username should have more than 1 char", 400)

        if len(password) < 1:
            return apology("Password should have more than 1 char", 400)

        if password != confirmation:
            return apology("Passwords dont't match", 400)

        # Check if username already in database
        if user_exists(username):
            return apology("A user with that username already exists", 400)

        # Try to add the user to db
        user_id = add_user(username, password)
        if not user_id:
            return apology("Something went wrong. Please try again.", 400)

        # Remember user adn redirect to home
        session["user_id"] = user_id
        return redirect("/")

    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
