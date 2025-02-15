from flask import Flask, render_template

# Create a Flask instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return "<h1>Hello, {}!</h1>".format(name)