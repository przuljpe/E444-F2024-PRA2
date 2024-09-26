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
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get("name")
        if old_name is not None and old_name != form.name.data:
            flash("Looks like you changed your name!")
        session["name"] = form.name.data
        session["email"] = form.email.data
        return redirect(url_for('index'))

    return render_template("index.html", form=form, name=session.get('name'), email=session.get('email'))

if __name__ == "__main__":
    app.run()