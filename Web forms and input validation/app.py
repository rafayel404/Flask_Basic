from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    flash
)
from forms import SignupForm,LogInForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "this_is_a_secret_key"

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title='Home')

@app.route('/signup', methods=['GET','POST'])
def signup():
    form=SignupForm()
    if form.validate_on_submit():
        flash(f"Successfully registered {form.username.data}!")
        return redirect(url_for("home"))
    return render_template('signup.html',title='Sign Up',form=form)
               
@app.route('/login',methods=['GET','POST'])
def login():
    form=LogInForm()
    if form.validate_on_submit():
        email=form.email.data
        pw=form.password.data
        if email == "a@b.com" and pw == "12345":
            flash("Logged in Successfully!")
            return redirect(url_for("home"))
        else:
            flash("Incorrect email or password")
    return render_template('login.html',title='LogIn',form=form)               

if __name__=='__main__':
    app.run(debug=True)