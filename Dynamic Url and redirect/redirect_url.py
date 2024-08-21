from flask import Flask,redirect,url_for
import time

app=Flask(__name__)

@app.route('/')
def home():
    return "Welcome to HomePage"

@app.route("/pass")
def passed():
    return "Congratulations, you have passed"

@app.route("/fail")
def failed():
    return "Sorry, you have failed"

@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num<30:
        time.sleep(1)
        return redirect(url_for("failed"))
    else:
        time.sleep(1)
        return redirect(url_for("passed"))
    

if __name__ == "__main__":
    app.run(debug=True)    