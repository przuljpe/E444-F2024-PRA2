from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, Regexp
import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "bruh momento"
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    email = StringField("What is your UofT email?", validators=[Email(), Regexp(".+utoronto.ca$")])
    submit = SubmitField("Submit")

@app.route('/', methods=["GET", "POST"])
def index():
    session["uoft"] = True
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get("name")
        old_email = session.get("email")
        if old_name is not None and old_name != form.name.data:
            flash("Looks like you changed your name!")
        if old_email is not None and old_email != form.email.data:
            flash("Looks like you changed your email!")
        session["name"] = form.name.data
        session["email"] = form.email.data
        return redirect(url_for('index'))
    return render_template("index.html", form=form, name=session.get('name'), email=session.get('email'), uoft=session.get('uoft'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')