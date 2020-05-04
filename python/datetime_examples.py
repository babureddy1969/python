from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
# Only days, seconds, and microseconds remain
print(delta)

d = timedelta(microseconds=-1)
print(d.days, d.seconds, d.microseconds)

delta1 = timedelta(seconds=57)
delta2 = timedelta(hours=25, seconds=2)
delta2 != delta1

delta2 == 5

# Components of another_year add up to exactly 365 days
year = timedelta(days=365)
another_year = timedelta(weeks=40, days=84, hours=23,
                         minutes=50, seconds=600)
year == another_year

year.total_seconds()

year = timedelta(days=365)
ten_years = 10 * year
ten_years

ten_years.days // 365

nine_years = ten_years - year
nine_years

three_years = nine_years // 3
three_years, three_years.days // 365

from datetime import date
date.fromisoformat('2019-12-04')

d = date(2002, 12, 31)
d.replace(day=26)
