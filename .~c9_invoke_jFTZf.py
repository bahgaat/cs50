import os
import datetime
from datetime import date
from cs50 import SQL
from flask import Flask,flash,jsonify,redirect,render_template,request,session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from itertools import chain

from helpers import apology, login_required
app = Flask(__name__)

#app.jinja_env.fiters["usd"]=usd

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


    


@app.route("/diet",methods=["GET","POST"])
@login_required
def diet():
    if request.method == "POST":
         
        food = request.form.get("food")
        quantity = request.form.get("quantity")
        Meal = request.form.get("Meal")
        if not food:
            return apology("must provide food",403)
        if not quantity:
            return apology("must provide password",400)
        if not Meal:
            return apology("must specify your gender",400)
        if quantity.isdigit():
            quantity = quantity
        else:
            return apology("must be an integer",400)
            
        userscalories = db.execute("SELECT totalgoalcalories,carbohydrategrams,proteingrams,fatgrams FROM usersinformation WHERE id=:id",
        id=session["user_id"])
        
        for totalcalories in userscalories:
            
            totalgoalcalories = float(totalcalories["totalgoalcalories"])
            carbohydrategrams = float(totalcalories["carbohydrategrams"])
            proteingrams = float(totalcalories["proteingrams"])
            fatgrams =float(totalcalories["fatgrams"])
        Totalgoalcalories = round(totalgoalcalories)
        Totalgoalcarb = round(carbohydrategrams)
        Totalgoalprotein = round(proteingrams)
        Totalgoalfat = round(fatgrams)
           
        if food == "Egg,boiled":
            fat = float(quantity)*0.11
            carb = float(quantity)*0.011
            protein = float(quantity)*0.13
            calories = float(fat)*9+float(carb)*4+float(protein)*4
        elif food == "Broad Bean":
            fat = float(quantity)*0.007
            carb = float(quantity)*0.18
            protein = float(quantity)*0.08
            calories = float(fat)*9+float(carb)*4+float(protein)*4
        elif food == "Cottage Cheese":
            fat = float(quantity)*0.043
            carb = float(quantity)*0.034
            protein = float(quantity)*0.11
            calories = float(fat)*9+float(carb)*4+float(protein)*4
        elif food == "Feta Cheese":
            fat = float(quantity)*0.21
            carb = float(quantity)*0.041
            protein = float(quantity)*0.14
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Falafel":
            fat = float(quantity)*0.18
            carb = float(quantity)*0.32
            protein = float(quantity)*0.13
            calories = float(fat)*9+float(carb)*4+float(protein)*4
        elif food == "Lunchon":
            fat = float(quantity)*0.32
            carb = float(quantity)*0.023
            protein = float(quantity)*0.13
            calories = float(fat)*9+float(carb)*4+float(protein)*4
        elif food == "TurkeyMeat":
            fat = float(quantity)*0.07
            carb = float(quantity)*0.01
            protein = float(quantity)*0.29
            calories = float(fat)*9+float(carb)*4+float(protein)*4
        elif food == "Oats":
            fat = float(quantity)*0.05
            carb = float(quantity)*0.51
            protein = float(quantity)*0.13
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Bread":
            fat = float(quantity)*0.0126
            carb = float(quantity)*0.52
            protein = float(quantity)*0.1
            calories = float(fat)*9+float(carb)*4+float(protein)*4
        elif food == "Halva(Halawa)":
            fat = float(quantity)*0.22
            carb = float(quantity)*0.6
            protein = float(quantity)*0.12
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Jam":
            fat = float(quantity)*0.001
            carb = float(quantity)*0.69
            protein = float(quantity)*0.004
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Turkey Meat":
            fat = float(quantity)*0.07
            carb = float(quantity)*0.01
            protein = float(quantity)*0.29
            calories = float(fat)*9+float(carb)*4+float(protein)*4
        elif food == "Honey":
            fat = float(quantity)*0
            carb = float(quantity)*0.82
            protein = float(quantity)*0.003
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Sugar":
            fat = float(quantity)*0
            carb = float(quantity)*1
            protein = float(quantity)*0
            calories = float(fat)*9+float(carb)*4+float(protein)*4
        elif food == "Milk":
            fat = float(quantity)*0.01
            carb = float(quantity)*0.05
            protein = float(quantity)*0.034
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Tomato":
            fat = float(quantity)*0.002
            carb = float(quantity)*0.039
            protein = float(quantity)*0.009
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Cucumber":
            fat = float(quantity)*0
            carb = float(quantity)*0.04
            protein = float(quantity)*0
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Potato":
            fat = float(quantity)*0.001
            carb = float(quantity)*0.17
            protein = float(quantity)*0.02
            calories = float(fat)*9+float(carb)*4+float(protein)*4
        elif food == "Carrot":
            fat = float(quantity)*0
            carb = float(quantity)*0.1
            protein = float(quantity)*0
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Tea":
            fat = float(quantity)*0
            carb = float(quantity)*0.002
            protein = float(quantity)*0.001
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Nescafe":
            fat = float(quantity)*0.002
            carb = float(quantity)*0.001
            protein = float(quantity)*0.004
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Coffee":
            fat = float(quantity)*0.
            carb = float(quantity)*0
            protein = float(quantity)*0.001
            calories = float(fat)*9+float(carb)*4+float(protein)*4
        elif food == "Orange Juice":
            fat = float(quantity)*0.002
            carb = float(quantity)*0.1
            protein = float(quantity)*0.007
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Olive Oil":
            fat = float(quantity)*1
            carb = float(quantity)*0
            protein = float(quantity)*0
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Oil":
            fat = float(quantity)*1
            carb = float(quantity)*0
            protein = float(quantity)*0
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Butter":
            fat = float(quantity)*0.81
            carb = float(quantity)*0
            protein = float(quantity)*0
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Salt":
            fat = float(quantity)*0
            carb = float(quantity)*0
            protein = float(quantity)*0
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Meat":
            fat = float(quantity)*0.035
            carb = float(quantity)*0
            protein = float(quantity)*0.26
            calories = float(fat)*9+float(carb)*4+float(protein)*4     
        elif food == "Grilled Chicken":
            fat = float(quantity)*0.15
            carb = float(quantity)*0.001
            protein = float(quantity)*0.23
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Fried Chicken":
            fat = float(quantity)*0.12
            carb = float(quantity)*0.018
            protein = float(quantity)*0.3
            calories = float(fat)*9+float(carb)*4+float(protein)*4
        elif food == "French Fries":
            fat = float(quantity)*0.15
            carb = float(quantity)*0.41
            protein = float(quantity)*0.034
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Tilapia Fish":
            fat = float(quantity)*0.027
            carb = float(quantity)*0
            protein = float(quantity)*0.26
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Mackerel Fish":
            fat = float(quantity)*0.18
            carb = float(quantity)*0
            protein = float(quantity)*0.24
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Salmon Fish":
            fat = float(quantity)*0.13
            carb = float(quantity)*0
            protein = float(quantity)*0.2
            calories = float(fat)*9+float(carb)*4+float(protein)*4
        elif food == "Canned Tuna":
            fat = float(quantity)*0.0821
            carb = float(quantity)*0
            protein = float(quantity)*0.29
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Rice,Cooked":
            fat = float(quantity)*0.003
            carb = float(quantity)*0.28
            protein = float(quantity)*0.027
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Pasta,Cooked":
            fat = float(quantity)*0.011
            carb = float(quantity)*0.25
            protein = float(quantity)*0.05
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Okra(Bamya)":
            fat = float(quantity)*0.002
            carb = float(quantity)*0.07
            protein = float(quantity)*0.019
            calories = float(fat)*9+float(carb)*4+float(protein)*4
        elif food == "Canned Tuna":
            fat = float(quantity)*0.0821
            carb = float(quantity)*0
            protein = float(quantity)*0.29
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Mulukhiyah":
            fat = float(quantity)*0.0025
            carb = float(quantity)*0.058
            protein = float(quantity)*0.0465
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Peas(besela)":
            fat = float(quantity)*0.004
            carb = float(quantity)*0.14
            protein = float(quantity)*0.05
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Cowpea(Fasoliya)":
            fat = float(quantity)*0.005
            carb = float(quantity)*0.21
            protein = float(quantity)*0.08
            calories = float(fat)*9+float(carb)*4+float(protein)*4
        elif food == "Spinach":
            fat = float(quantity)*0
            carb = float(quantity)*0.01
            protein = float(quantity)*0.009
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Taro(Qolqas)":
            fat = float(quantity)*0.002
            carb = float(quantity)*0.26
            protein = float(quantity)*0.015
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Apple":
            fat = float(quantity)*0.002
            carb = float(quantity)*0.14
            protein = float(quantity)*0.003
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Orange":
            fat = float(quantity)*0.001
            carb = float(quantity)*0.12
            protein = float(quantity)*0.009
            calories = float(fat)*9+float(carb)*4+float(protein)*4
        elif food == "Banana":
            fat = float(quantity)*0.003
            carb = float(quantity)*0.23
            protein = float(quantity)*0.011
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Cantaloupe":
            fat = float(quantity)*0.002
            carb = float(quantity)*0.08
            protein = float(quantity)*0.008
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Watermelon":
            fat = float(quantity)*0.002
            carb = float(quantity)*0.08
            protein = float(quantity)*0.006
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Grapes":
            fat = float(quantity)*0.004
            carb = float(quantity)*0.17
            protein = float(quantity)*0.006
            calories = float(fat)*9+float(carb)*4+float(protein)*4
        elif food == "Strawberry":
            fat = float(quantity)*0.003
            carb = float(quantity)*0.08
            protein = float(quantity)*0.007
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Muskmelon(Shamam)":
            fat = float(quantity)*0.002
            carb = float(quantity)*0.08
            protein = float(quantity)*0.008
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Avocado":
            fat = float(quantity)*0.15
            carb = float(quantity)*0.09
            protein = float(quantity)*0.02
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Pineapples":
            fat = float(quantity)*0.001
            carb = float(quantity)*0.13
            protein = float(quantity)*0.005
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Milk Chocolate":
            fat = float(quantity)*0.3
            carb = float(quantity)*0.59
            protein = float(quantity)*0.08
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Dark Chocolate":
            fat = float(quantity)*0.31
            carb = float(quantity)*0.61
            protein = float(quantity)*0.049
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Pop Corn":
            fat = float(quantity)*0.043
            carb = float(quantity)*0.74
            protein = float(quantity)*0.11
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Chipse":
            fat = float(quantity)*0.35
            carb = float(quantity)*0.53
            protein = float(quantity)*0.07
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "White Egg":
            fat = float(quantity)*0.002
            carb = float(quantity)*0.007
            protein = float(quantity)*0.11
            calories = float(fat)*9+float(carb)*4+float(protein)*4       
        elif food == "Chicken Breast":
            fat = float(quantity)*0.036
            carb = float(quantity)*0
            protein = float(quantity)*0.31
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Egg,fried":
            fat = float(quantity)*0.15
            carb = float(quantity)*0.008
            protein = float(quantity)*0.14
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Liver":
            fat = float(quantity)*0.044
            carb = float(quantity)*0.038
            protein = float(quantity)*0.26
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Apricots":
            fat = float(quantity)*0.004
            carb = float(quantity)*0.11
            protein = float(quantity)*0.014
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Peach":
            fat = float(quantity)*0.003
            carb = float(quantity)*0.1
            protein = float(quantity)*0.009
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        elif food == "Plums":
            fat = float(quantity)*0.003
            carb = float(quantity)*0.11
            protein = float(quantity)*0.007
            calories = float(fat)*9+float(carb)*4+float(protein)*4 
        fat = round(fat)
        carb = round(carb)
        protein = round(protein)
        calories = round(calories)
        empty = " "
        dict = {}
        if Meal == "Breakfast":
            dict['Breakfast'] = food
        else:
            dict['Breakfast'] = empty
        if Meal == "Lunch":
            dict['Lunch'] = food
        else:
            dict['Lunch'] = empty
        if Meal == "Dinner":
            dict['Dinner'] = food
        else:
            dict['Dinner'] = empty
        if Meal == "Snacks":
            dict['Snacks'] = food  
        else:
            dict["Snacks"] = empty
        
        selectdate = db.execute("SELECT * FROM usersgoals WHERE id=:id",
        id=session["user_id"]
        
        
        for new in selectdate:
            date = x["date"]
        date_time_str = date
        date_time_obj = datetime.datetime.strptime(date_time_str, '%d-%m-%Y')
            
        print(date_time_obj)
       
        today = date.today()
        
        print(today)
        
        if today > date_time_obj:
            
            deleteusersgoals = db.execute("DELETE FROM usersgoals WHERE id=:id",
            id=session["user_id"])
            
            newusersgoal = db.execute("INSERT INTO usersgoals(id,Breakfast,Dinner,Lunch,Snacks,Totalgoalcalories,Totalgoalfat,Totalgoalcarb,Totalgoalprotein,Calories,Fat,Carb,Protein,date)VALUES(:id,:Breakfast,:Dinner,:Lunch,:Snacks,:Totalgoalcalories,:Totalgoalfat,:Totalgoalcarb,:Totalgoalprotein,:calories,:fat,:carb,:protein,date('now','localtime'))",
            id=session["user_id"],Breakfast=dict["Breakfast"],Dinner=dict["Dinner"],Lunch=dict["Lunch"],Snacks=dict["Snacks"],Totalgoalcalories=Totalgoalcalories,Totalgoalfat=Totalgoalfat,Totalgoalcarb=Totalgoalcarb,Totalgoalprotein=Totalgoalprotein,calories=calories,fat=fat,carb=carb,protein=protein)

        updateusersgoal = db.execute("SELECT Breakfast,Dinner,Lunch,Snacks,Totalgoalcalories,Totalgoalfat,Totalgoalcarb,Totalgoalprotein,Calories,Fat,Carb,Protein FROM usersgoals WHERE id=:id  ",
        id=session["user_id"])
        
        updateusersgoal2 = db.execute("SELECT SUM(Calories),Totalgoalcalories-SUM(Calories),SUM(Fat),Totalgoalfat-SUM(Fat),SUM(Carb),Totalgoalcarb-SUM(Carb),SUM(Protein),Totalgoalprotein-SUM(Protein) FROM usersgoals WHERE id=:id",
        id=session["user_id"])
        
        for calories in updateusersgoal2:
            Caloriesconsumed = calories["SUM(Calories)"]
            Remainingcalories = calories["Totalgoalcalories-SUM(Calories)"]
            Fatconsumed = calories["SUM(Fat)"]
            Remainingfat = calories["Totalgoalfat-SUM(Fat)"]
            Carbconsumed = calories["SUM(Carb)"]
            Remainingcarb = calories["Totalgoalcarb-SUM(Carb)"]
            Proteinconsumed = calories["SUM(Protein)"]
            Remainingprotein = calories["Totalgoalprotein-SUM(Protein)"]
        
        for total in updateusersgoal:
            Totalgoalcalories = total["Totalgoalcalories"]
            Totalgoalfat = total["Totalgoalfat"]
            Totalgoalcarb = total["Totalgoalcarb"]
            Totalgoalprotein = total["Totalgoalprotein"]
            
        return render_template("plan.html",Totalgoalcalories=Totalgoalcalories,Totalgoalfat=Totalgoalfat,Totalgoalcarb=Totalgoalcarb,Totalgoalprotein=Totalgoalprotein,updateusersgoal =updateusersgoal,Caloriesconsumed=Caloriesconsumed,Remainingcalories=Remainingcalories,Fatconsumed=Fatconsumed,Remainingfat=Remainingfat,Carbconsumed=Carbconsumed,Remainingcarb=Remainingcarb,Proteinconsumed=Proteinconsumed,Remainingprotein=Remainingprotein)
    else:
        return("diet.html")
        
@app.route("/register",methods=["GET","POST"])
def register():
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username",403)
        if not request.form.get("password"):
            return apology("must provide password",400)
        if not request.form.get("gender"):
            return apology("must specify your gender",400)
        if not request.form.get("activity"):
            return apology("must choose an activity",400)
        if not request.form.get("age"):
            return apology("mist choose an age",400)
        if not request.form.get("height"):
            return apology("must choose an height",400)
        if not request.form.get("weight"):
            return apology("must choose a weight",400)
        if not request.form.get("goal"):
            return apology("write your weight",400)
        if not request.form.get("bodyfat"):
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
            
        bodyfat = request.form.get("bodyfat")
        gender = request.form.get("gender")
        activity = request.form.get("activity")
        caloriesfemale = float(weight)*0.9*24
        caloriesmale = float(weight)*1*24
        goal = request.form.get("goal")
        
        
          
        if gender=="female" and bodyfat == "14-18":
            BMR = float(caloriesfemale)*1.00
             
        elif gender=="female" and bodyfat == "19-28" :
            BMR = float(caloriesfemale) * 0.95
             
        elif gender=="female" and bodyfat == "29-38" :
            BMR = float(caloriesfemale) *0.90
         
        elif gender=="female" and bodyfat == "over38" :
            BMR = float(caloriesfemale) *0.85
                
       
        elif gender=="male" and bodyfat == "10-14" :
            BMR = float(caloriesmale) * 1.0
          
        elif gender=="male" and bodyfat == "15-20":
            BMR = float(caloriesmale) * 0.95
         
        elif gender=="male" and  bodyfat == "21-28":
            BMR = float(caloriesmale) *0.90
           
        elif gender=="male" and bodyfat == "over28" :
            BMR = float(caloriesmale) *0.85
        BMR = BMR   
               
        if activity == "verylight":
            totalcalories = float(BMR) * 1.3
               
        elif activity == "light":
            totalcalories = float(BMR) * 1.55
               
        elif activity == "moderate":
            totalcalories = float(BMR) * 1.65
         
        elif activity == "heavy":
            totalcalories = float(BMR) * 1.80
             
        elif activity == "veryheavy":
            totalcalories = float(BMR) * 2.00
        totalcalories = totalcalories
              
        if goal == "lose":
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
        
        carbohydratecalories = float(totalgoalcalories)/2.5
        proteincalories = float(totalgoalcalories)/2.5
        fatcalories = float(totalgoalcalories)/5
        
        carbohydrategrams = float(carbohydratecalories)/4
        proteingrams = float(proteincalories)/4
        fatgrams = float(fatcalories)/9
        
        hash = generate_password_hash(request.form.get("password"))    
        usersinformation = db.execute("INSERT INTO usersinformation(hash,weight,height,age,username,gender,activity,bodyfat,totalgoalcalories,carbohydrategrams,proteingrams,fatgrams)VALUES (:hash,:weight,:height,:age,:username,:gender,:activity,:bodyfat,:totalgoalcalories,:carbohydrategrams,:proteingrams,:fatgrams)", 
        username=request.form.get("username"),hash=hash,weight=weight,height=height,age=age,gender=gender,activity=activity,bodyfat=bodyfat,totalgoalcalories=totalgoalcalories,carbohydrategrams=carbohydrategrams,proteingrams=proteingrams,fatgrams=fatgrams)
        if not usersinformation:
            return apology("choose another name",400)
                        
                            
        session["user_id"] = usersinformation
        
        return render_template("diet.html")
           
    else:
        return render_template("register.html")

@app.route("/login",methods=["GET","POST"])
def login():
    #forget any users id
    session.clear() 
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username",403)
        if not request.form.get("password"):
            return apology("must provide password",403)
        usersinformation = db.execute("SELECT * FROM usersinformation WHERE username=:username",
        username = request.form.get("username"))
        
        if len(usersinformation) != 1 or not check_password_hash(usersinformation[0]["hash"],request.form.get("password")):
            return apology("invalid username and/or password",403)
        
        session["user_id"] = usersinformation[0]["id"]
        
        return render_template("diet.html")
    else:
        return render_template("login.html")
            
            
            
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
    session.clear()
    
    return render_template("login.html")

def errorhandler(e):
    if not isinstance(e,HTTPException):
        e = InternalServerError()
    return apology(e.name,e.code)
    
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)