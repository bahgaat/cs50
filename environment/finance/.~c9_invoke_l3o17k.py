import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd
from itertools import chain

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


@app.route("/")
@login_required
def index():

    stocks = db.execute("SELECT Symbol,Name,Shares,Price,Total FROM portfolio WHERE id=:id",
    id=session["user_id"])





    Symbol = db.execute("SELECT Symbol FROM portfolio WHERE id=:id",
    id=session["user_id"])
    Name = db.execute("SELECT Name FROM portfolio WHERE id=:id",
    id=session["user_id"])
    Shares = db.execute("SELECT Shares FROM portfolio WHERE id=:id",
    id=session["user_id"])
    Price = db.execute("SELECT Price FROM portfolio WHERE id=:id",
    id=session["user_id"])
    Total = db.execute("SELECT Total From portfolio WHERE id=:id",
    id=session["user_id"])









    return render_template("index.html",stocks=stocks)










@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    #if user reached via post
    if request.method == "POST":
        #make variables to facilitate it to me
        stock = request.form.get("stock")
        shares = request.form.get("shares")
        int_shares = int(shares)

        # Ensure stock is submitted
        if not stock:
            return apology("must write a name of a stock",403)

        # Ensure number of shares is submittes
        elif not shares :
            return apology("must provide how many do you want to purchase",403)

        #Ensure that the number is positive
        elif int_shares < 1 :
            return apology("must be a positive number",403)


        #select their money from the database
        list = db.execute("SELECT cash FROM users WHERE id=:id",
        id=session["user_id"])
        t = list[0]
        y = t['cash']
        r = int(y)







        #obtain the price,name, and symbol of the product form lookup function
        dict ={}
        dict = lookup(stock)
        price = dict['price']
        symbol  = dict['symbol']
        name = dict['name']
        total = price*int_shares

        #Ensure that the user has sufficient money
        if total <= r:

           #add the stock name and the username and the price to the portfolio database
           portfolio = db.execute("INSERT INTO portfolio(symbol,name,shares,price,total,id)VALUES(:name,:symbol,:int_shares,:price,:total,:id)",
           symbol=symbol,name=name,int_shares=int_shares,price=price,total=total,id=session["user_id"])

           #update1 = db.execute("update portfolio SET shares = shares+:int_shares WHERE id=:id and symbol=:symbol",
           #symbol=symbol,int_shares=int_shares,id=session["user_id"])
           #update user cash

           update = db.execute('UPDATE users SET cash = :r - :total WHERE id=:id',
           r = r, total=total,id=session["user_id"])
           return render_template("index.html")
        else:
            return apology("not enough money",403)



    #if user via get means without clicking submit
    else:
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
#@login_required
def quote():
    if request.method == "POST":
        if not request.form.get("symbol"):
            return apology("choose a stock", 403)
        dict = {}
        symbol = request.form.get("symbol")
        dict = lookup(symbol)
        return render_template("stock.html",stock = dict)
    else:
        return render_template("quote.html")






    """Get stock quote."""




@app.route("/register", methods=["GET", "POST"])
def register():





    """Register user"""
    if request.method == "POST":

        if not request.form.get("username"):
            return apology("must provide username", 403)
        elif not request.form.get("password"):
            return apology("must provide password", 403)
        elif not request.form.get("re confirm password"):
            return apology("must reconfirm password", 403)
        elif request.form.get("password") != request.form.get("re confirm password"):
            return apology("password must be the same ",403)



        hash=generate_password_hash(request.form.get("password"))




        result = db.execute(
        "INSERT INTO users (username,hash)VALUES(:username,:hash)",
        username = request.form.get("username"), hash =hash)

        if not result:
            return apology("Try another username",403)



        session["user_id"] = result

        return redirect("/")

    else:

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
