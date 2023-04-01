
import random
import time
import datetime
import calendar

def getMonthsAndDaysName(my_dates):
    my_dates['months'] = list(calendar.month_abbr)[1:]
    my_dates['days'] = list(calendar.day_abbr)
    my_dates['currentYear'] = datetime.date.today().year
    print(my_dates['months'], my_dates['days'], my_dates['currentYear'])


def isLeapYear(year):
    if year%4 == 0 and (year%100 != 0 or year%400 == 0):
        return True
    else:
        return False


def getRandomDate():
    randomDay = random.randint(1, 31)
    randomMonth = random.randint(0, 11)        
    my_dates = {
      'months': [],
      'days': [],
      'currentYear': None   
    }

    getMonthsAndDaysName(my_dates)
    print("-----------------")
    print(my_dates['months'], my_dates['days'], my_dates['currentYear'])
    print("-----------------")

    # February will be 29 in leap year
    # month index starts with 0
    if randomMonth == 1:
      if randomDay > 28:
          if isLeapYear(my_dates['currentYear']):
              print("It is a leap year and fabruary can be of 29 days")
              randomDay = 29
          else:
              randomDay = 28


    randomDate = f"{randomDay}-{my_dates['months'][randomMonth]}-{my_dates['currentYear']}"
    return randomDate



print("Let's print the months of year")
time.sleep(1)

randomDate = getRandomDate()
print("Your appointment is on: ", randomDate)

