from flask import Flask,render_template,url_for
import time
from employees import employees_data
app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title='Home page')

@app.route('/about')
def about():
    return render_template('about.html',title='About page')

@app.route('/employees')
def employees():
    return render_template('employees.html',title='Employees page',
                           emps=employees_data)

@app.route('/evaluate/<int:num>')
def evaluate(num):
    return render_template('evaluate.html',
                           title='Evaluate page',
                           number=num)
    
 
if __name__ == "__main__":
    app.run(debug=True)     