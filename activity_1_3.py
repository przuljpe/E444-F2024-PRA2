from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    date = datetime.datetime.now(datetime.timezone.utc)
    return render_template("user.html", current_time=date)

if __name__ == "__main__":
    app.run()