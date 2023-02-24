import math
import datetime

#return days left in exam
date = "2023-02-28"

def days_left(date):
    #convert date to datetime object
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    #get current date
    today = datetime.datetime.now()
    #calculate days left
    days_left = date - today
    #return days left
    return days_left.days

print(days_left(date))


