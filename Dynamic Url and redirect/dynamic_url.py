from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "welcome to home"

@app.route("/welcome/<name>")
def welcome_steve(name):
    return f"Hey {name.title()} ,welcome to our page"



if __name__=="__main__":
    app.run(debug=True)