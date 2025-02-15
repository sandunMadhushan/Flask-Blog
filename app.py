from flask import Flask, render_template

# Create a Flask instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')

def index():
    first_name = 'John'
    return render_template('index.html', first_name=first_name)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)