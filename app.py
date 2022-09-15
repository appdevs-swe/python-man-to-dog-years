from flask import (Flask, render_template, url_for)
from datetime import date, datetime
from dateutil import relativedelta
from numpy import log

app = Flask(__name__)

@app.route("/")

def welcome():
    date_born_long=datetime(2021,10,31)
    date_born=date_born_long.date()
    
    date_today=date.today()

    diff = relativedelta.relativedelta(date_today, date_born)

    years = diff.years
    months = diff.months
    days = diff.days

    decimal_year = ((years*12)+months)/12
   
    dog_years = round(16 * log(decimal_year) + 31,1)

    return render_template(
        "welcome.html", man_years=years, man_months=months, man_days=days, born=date_born, todays_date=date_today,display_dog_years=dog_years, 
    )

if __name__ == "__main__":
    app.run(debug=True)
