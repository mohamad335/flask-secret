from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired
class MyForm(FlaskForm):
    email= StringField('Email',validators= [DataRequired()])
    password= PasswordField('Password', validators= [DataRequired()]) 
    submit= SubmitField('Log In')
app = Flask(__name__)
app.secret_key= "dalal"

@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)
if __name__ == '__main__':
    app.run(debug=True)
