from cs50 import SQL
from flask import Flask, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, usd, lookup, convert
import time
import os

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

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

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
        shares = convert(request.form.get("shares"), int)
        uid = session.get("user_id")

        if None in (symbol, shares, uid) or shares < 0:
            return apology("Invalid request")

        # Get necessary data
        res = lookup(symbol)
        if res is None:
            return apology("Invalid request")

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
    else:
        return render_template("buy.html")


@app.route("/check", methods=["GET"])
def check():
    """Return true if username available and 1 character or more, else false, in JSON format"""
    if len(request.args.get("username")) <= 0 or not username_available(request.args.get("username")):
        return jsonify(False)

    return jsonify(True)


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    uid = session.get("user_id")
    transactions = get_transactions(uid)
    return render_template("history.html", transactions=transactions)


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


    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure no blanks in form data and that passwords matched
        if not request.form.get("username"):
            return apology("No Username")

        elif not request.form.get("password"):
            return apology("No PAssword")

        elif not request.form.get("confirmation"):
            return apology("Passwords do not match")

        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("Passwords do not match")

        # Check if username already in database
        if not username_available(request.form.get("username")):
            return apology("username already taken")

        # Add new user to database
        # ID auto increments
        db.execute('INSERT INTO "users" ("id","username","hash") VALUES (NULL, :username, :hash)',
                   username=request.form.get("username"),
                   hash=generate_password_hash(request.form.get("password")))

        # Query database to get users id
        rows = db.execute("SELECT id FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/change_pw", methods=["GET", "POST"])
@login_required
def change_pw():
    if request.method == "POST":

        if not request.form.get("password"):
            return apology("No PAssword")

        elif not request.form.get("confirmation"):
            return apology("Passwords do not match")

        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("Passwords do not match")

        db.execute("UPDATE users SET hash = :hash WHERE id= :uid", uid=session["user_id"],
                   hash=generate_password_hash(request.form.get("password")))
        # Redirect user to home page
        return redirect("/logout")

    else:
        return render_template("change_pw.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    uid = session.get("user_id")

    if request.method == "POST":
        # Form validation
        symbol = request.form.get("symbol")
        shares = convert(request.form.get("shares"), int)

        if None in (symbol, shares, uid) or shares < 0:
            return apology("Invalid request")

        # Get necessary data
        res = lookup(symbol)
        if res is None:
            return apology("Invalid request")

        name, price, symbol = res.values()

        stocks = query_stock(uid, symbol)[0]

        # Check user has enough stocks
        if shares > stocks['shares']:
            return apology(f"Too many shares selected")

            # Check users credit balance
        user = get_user_by_id(uid)
        if user is None or len(user) == 0:
            return apology("Could not lookup data")

        cash = user[0]["cash"]

        new_cash = cash + price * shares

        # ATTENTION - NOT SAFE: If the first operation succeeds and the second fails,
        # the database will get corrupted!
        #
        # How to fix: Use some framework like sqlalchemy, to be able to rollback transactions
        # or commit after both operations succeed
        if False in (
                update_user_cash(uid, new_cash), add_transaction(uid, symbol, shares, price, buy_or_sell=False),
                remove_stock(uid, symbol, shares)):
            return apology("Could not process transaction")

        # Redirect user to home page
        return redirect("/")

    else:
        # Get users stocks
        stocks = query_stock(uid=uid)

        return render_template("sell.html", stocks=stocks)


def username_available(username):
    '''Return true if username is available, false if not'''
    return len(db.execute("SELECT username FROM users WHERE username = :username", username=username)) == 0


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)


def get_user_by_id(uid):
    """
    Get user by name
    """
    return db.execute("SELECT id,username,cash FROM users WHERE id = :uid", uid=uid)


def update_user_cash(uid, new_cash):
    """ Update cash of user"""
    db.execute("UPDATE users SET cash = :new_cash WHERE id = :uid",
               new_cash=new_cash,
               uid=uid)
    return True


def add_transaction(uid, symbol, shares, price, buy_or_sell=True):
    """ Add a transaction """
    db.execute('''INSERT INTO transactions (id, uid, symbol, shares, transaction_time, price, buy)
                  VALUES (NULL, :uid, :symbol, :shares, :transaction_time, :price, :buy_or_sell)''',
               uid=uid,
               symbol=symbol,
               shares=shares,
               transaction_time=time.strftime('%Y-%m-%d %H:%M:%S'),
               price=price,
               buy_or_sell=buy_or_sell)
    return True


def add_stock(uid, symbol, shares):
    """ Add new stock to user into stocks table """
    # check if user has already symbol stocks
    t = db.execute("SELECT * FROM stocks WHERE uid= :uid AND symbol=:symbol; ", uid=uid, symbol=symbol)
    if t:
        new_shares = t[0]['shares'] + shares
        db.execute("UPDATE stocks SET shares = :shares WHERE uid= :uid and symbol=:symbol", uid=uid, symbol=symbol, shares=new_shares)
    else:
        db.execute("INSERT INTO stocks (id, uid, symbol, shares) VALUES (NULL, :uid, :symbol, :shares)", uid=uid, shares=shares,
                   symbol=symbol)
    return True


def remove_stock(uid, symbol, shares):
    # check if user has already symbol stocks
    t = db.execute("SELECT * FROM stocks WHERE uid= :uid AND symbol=:symbol; ", uid=uid, symbol=symbol)[0]
    new_shares = t['shares'] - shares
    if new_shares > 0:
        db.execute("UPDATE stocks SET shares = :shares WHERE uid= :uid and symbol=:symbol", uid=uid, symbol=symbol, shares=new_shares)
    else:
        db.execute("DELETE FROM stocks WHERE uid= :uid and symbol=:symbol", uid=uid, symbol=symbol)
    return True


def query_stock(uid, symbol=None):
    """ Query stock table"""
    if symbol:
        return db.execute("SELECT * FROM stocks WHERE uid= :uid AND symbol=:symbol; ", uid=uid, symbol=symbol)
    return db.execute("SELECT * FROM stocks WHERE uid= :uid; ", uid=uid)


def get_transactions(uid):
    return db.execute("SELECT * FROM transactions WHERE uid=:uid ORDER BY ID DESC; ", uid=uid)
