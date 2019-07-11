import os
from cs50 import SQL
from flask import Flask,flash,jsonify,redirect,render_template,request,session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from itertools import chain

from helpers import apology, login_required
app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"]=True

@app.after_request
def after_request(response):
    
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response
    
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db= SQL("sqlite:///bahgat.db")


    


@app.route("/")
@login_required
def diet():
    return apology("fff",400)

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username",403)
        elif not request.form.get("password"):
            return apology("must provide password",400)
        elif not request.form.get("gender"):
            return apology("must specify your gender",400)
        elif not request.form.get("activity"):
            return apology("must choose an activity",400)
        elif not request.form.get("age"):
            return apology("mist choose an age",400)
        elif not request.form.get("height"):
            return apology("must choose an height",400)
        elif not request.form.get("weight"):
            return apology("must choose a weight",400)
        elif not request.form.get("goal"):
            return apology("write your weight",400)
        elif not request.form.get("body fat"):
            return apology("write your body fat",400)
        age = request.form.get("age")
        height = request.form.get("height")
        weight = request.form.get("weight")
       
        if float(age)<1 :
            return apology("it must be positive",400)
            
        if float(height)<1:
            return apology("must be positive",400)

        if float(weight)<1:
            return apology("must be positive",400)
        bodyfat = request.form.get("body fat")
        gender = request.form.get("gender")
        activity = request.form.get("activity")
        caloriesfemale = float(weight)*0.9*24
        caloriesmale = float(weight)*1*24
        goal = request.form.get("goal")
        if gender=="female":
            caloriesfemale = float(weight)*0.9*24
            
            if bodyfat == "14-18(female":
                BMR = float(caloriesfemale)*1.00
                
            if bodyfat == "19-28(female)" :
                BMR = float(caloriesfemale) * 0.95
                
            if bodyfat == "29-38(female)" :
                BMR = float(caloriesfemale) *0.90
      
            if bodyfat == "over38(female)" :
                BMR = float(caloriesfemale) *0.85
                
        elif gender == "male":
            caloriesfemale = float(weight)*1.0*24
            
            if bodyfat == "10-14(male)" :
                BMR = float(caloriesmale) * 1.0
        
            if bodyfat == "15-20(male)":
                BMR = float(caloriesmale) * 0.95
       
            if bodyfat == "21-28(male)":
                BMR = float(caloriesmale) *0.90
      
            if bodyfat == "over28(male)" :
                BMR = float(caloriesmale) *0.85
        
                if activity == "verylight":
                    totalcalories = float(BMR) * 1.3
                elif activity == "light":
                    totalcalories = float(BMR) * 1.55
                elif activity == "moderate":
                    totalcalories = float(BMR) * 1.65
                elif activity == "heavy":
                    totalcalories = float(BMR) * 1.80
                if activity == "veryheavy":
                    totalcalories = float(BMR) * 2.00
                    goal = request.form.get("goal")
                    if goal == "lose0.25kg":
                        totalgoalcalories = float(totalcalories) - 250
                    elif goal == "lose0.5kg":
                        totalgoalcalories = float(totalcalories) - 500
                    elif goal == "maintainmyweight":
                        totalgoalcalories = float(totalcalories) 
                    elif goal == "gain0.25kg":
                        totalgoalcalories = float(totalcalories) + 250
                    elif goal == "gain0.5kg":
                        totalgoalcalories = float(totalcalories) +500
                    totalgoalcalories = totalgoalcalories
                    hash = generate_password_hash(request.form.get("password"))
                    users = db.execute("INSERT INTO users(username,password,weight,height,age,sex,activity,bodyfat,goal,totalgoalcalories)VALUES(:username,:hash,:weight,:height,:age,:gender,:activity,:bodyfat,:goal,:totalgoalcalories)",
                    username=request.form.get("username"),hash=hash,weight=weight,height=height,age=age,goal=goal,gender=gender,activity=activity,bodyfat=bodyfat,totalgoalcalories=totalgoalcalories)
                    if not users:
                        return apology("choose another name",400)
        
                    session["user_id"] = users
                    return render_template("register.html")
    else:
        return render_template("register.html")

@app.route("/login",methods=["GET","POST"])
def login():
    return apology("gg",400)
    
@app.route("/advices",methods=["GET","POST"])
def advices():
    return apology("kk",400)
    
@app.route("/changes",methods=["GET","POST"])
def changes():
    return apology("kk",400)

@app.route("/history",methods=["GET","POST"])
def history():
    return apology("gg",400)
    
@app.route("/search",methods=["GET","POST"])
def search():
    return apology("kk",400)
    
@app.route("/logout",methods=["GET","POST"])
def logout():
    return apology("pp",400)
