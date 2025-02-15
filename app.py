from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Create a Flask instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'my super secret key'

# Create a form class
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Define a route for the home page
@app.route('/')

def index():
    first_name = 'John'
    return render_template('index.html', first_name=first_name)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)

# Create custom error pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal server error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Create name page
@app.route('/name', methods=['GET', 'POST'])

def name():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('name.html', name=name, form=form)