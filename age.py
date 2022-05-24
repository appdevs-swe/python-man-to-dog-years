# Ref code - not used in app
from datetime import date, datetime
from numpy import log
import numpy as np

date_born = "2021-10-31"
date_today = str(date.today())

start = datetime.strptime(date_born, "%Y-%m-%d")
end = datetime.strptime(date_today, "%Y-%m-%d")

delta = end.date()-start.date()
print(delta.days)

decimal_year = delta.days / 31 / 12
print(decimal_year)
man_years = 16 * log(decimal_year) + 31
print(man_years)
#print(f"Alice är {years} år och {months} månader")
#print("Det motsvarar " + str(int(man_years)) + " hundår")
#adding comment to see change in remote