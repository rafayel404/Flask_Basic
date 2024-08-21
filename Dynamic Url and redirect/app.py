from flask import Flask

app=Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "Welcome to the page"

@app.route("/about")
def about():
    return "Welcome to the about page"


if __name__=="__main__":
    app.run(debug=True)