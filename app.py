from ast import If
from flask import (Flask, render_template, url_for)
from datetime import date, datetime
from numpy import log

app = Flask(__name__)

@app.route("/")
def welcome():
    date_born = "2021-10-31"
    date_today = str(date.today())

    start = datetime.strptime(date_born, "%Y-%m-%d")
    end = datetime.strptime(date_today, "%Y-%m-%d")

    delta = end.date()-start.date()
    num_months = (end.year - start.year) * 12 + (end.month - start.month) -1
    years, months = divmod(num_months, 12)
    
    decimal_year = delta.days / 30.5 / 12
    calendar_years = 16 * log(decimal_year) + 31

    return render_template(
        "welcome.html", man_years=years, man_months=months, display_dog_years=int(calendar_years), born=date_born, todays_date=date_today, 
    )


