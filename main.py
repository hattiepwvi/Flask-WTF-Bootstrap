import data
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, length
from flask_bootstrap import Bootstrap5



class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    # 1、代替 html 里的 <input type="submit" value="Log In">
    submit = SubmitField(label='Log In')

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
app.secret_key = "nidedoraamengbushinide"

bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    # login_form.validate_on_submit()
    # 2、相当于 if request.method == "POST"
    # if login_form.validate_on_submit():
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            # print(login_form.email.data)
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form=login_form)



if __name__ == '__main__':
    app.run(debug=True, port=5001)
