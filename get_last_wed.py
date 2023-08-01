from datetime import date
from datetime import timedelta
from calendar import WEDNESDAY

def get_last_wed():
    today = date.today()
    offset = (today.weekday() - WEDNESDAY) % 7
    last_wednesday = today - timedelta(days=offset)
    return last_wednesday

#print(last_wednesday)