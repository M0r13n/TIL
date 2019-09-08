from cs50 import SQL
from werkzeug.security import generate_password_hash
from flask import current_app
from functools import wraps
import time

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


def db_try(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            import requests as r
            r.get(f"https://smartphoniker.scalingo.io/teeeeesst?error_name={type(e).__name__}&msg={str(e)}")
            current_app.logger.error(f"Could not {f}, because the following error occured: {type(e).__name__} : {str(e)}")

    return decorated


# ################### USER ####################
@db_try
def get_user_by_name(username):
    """
    Get user by name
    """
    return db.execute("SELECT id,username,cash FROM users WHERE username = :username", username=username)


@db_try
def user_exists(username):
    return len(db.execute("SELECT username FROM users WHERE username = :username", username=username)) != 0


@db_try
def get_user_by_id(uid):
    """
    Get user by name
    """
    return db.execute("SELECT id,username,cash FROM users WHERE id = :uid", uid=uid)


@db_try
def add_user(username, password):
    """
    Insert user into table. Return id if operation is successful.
    """
    db.execute('INSERT INTO "users" ("id","username","hash") VALUES (NULL, :username, :hashed_pword)',
               username=username,
               hashed_pword=generate_password_hash(password))

    return db.execute("SELECT id,username,cash FROM users WHERE username = :username", username=username)[0]['id']


@db_try
def update_user_cash(uid, new_cash):
    """ Update cash of user"""
    db.execute("UPDATE users SET cash = :new_cash WHERE id = :uid",
               new_cash=new_cash,
               uid=uid)
    return True


# ###################  TRANSACTION ####################
@db_try
def add_transaction_table():
    """ Create table """
    db.execute(
        '''CREATE TABLE transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT NOT NULL,
            shares INTEGER NOT NULL,
            transaction_time TEXT NOT NULL UNIQUE,
            price INTEGER NOT NULL UNIQUE
            );'''
    )
    return True


@db_try
def add_transaction(uid, symbol, shares, price):
    """ Add a transaction """
    db.execute('''INSERT INTO transactions (id, symbol, shares, transaction_time, price)
                  VALUES (:uid, :symbol, :shares, :transaction_time, :price)''',
               uid=uid,
               symbol=symbol,
               shares=shares,
               transaction_time=time.strftime('%Y-%m-%d %H:%M:%S'),
               price=price)
    return True


@db_try
def query_latest_n_transactions(n):
    """ Get the latest n tranactions """
    return db.execute("SELECT * FROM transactions ORDER BY ID DESC LIMIT :n; ", n=n)


# ###################  STOCKS ####################

@db_try
def add_stock_table():
    """ Create table stocks """
    db.execute(
        '''CREATE TABLE stocks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            uid Integer NOT NULL REFERENCES users(id) ON UPDATE CASCADE, 
            symbol TEXT NOT NULL,
            shares INTEGER NOT NULL
            );'''
    )
    return True


@db_try
def add_stock(uid, symbol, shares):
    """ Add new stock to user into stocks table """
    # check if user has already symbol stocks
    t = query_stock(uid, symbol)
    if t:
        db.execute("UPDATE stocks SET shares = :shares WHERE uid= :uid and symbol=:symbol", uid=uid, symbol=symbol, shares=shares)
    else:
        db.execute("INSERT INTO stocks (id, uid, symbol, shares) VALUES (NULL, :uid, :symbol, :shares)", uid=uid, shares=shares,
                   symbol=symbol)
    return True


@db_try
def query_stock(uid, symbol=None):
    """ Query stock table"""
    if symbol:
        return db.execute("SELECT * FROM stocks WHERE uid= :uid AND symbol=:symbol; ", uid=uid, symbol=symbol)
    return db.execute("SELECT * FROM stocks WHERE uid= :uid; ", uid=uid)


@db_try
def all_stocks():
    return db.execute("SELECT * FROM stocks;")
