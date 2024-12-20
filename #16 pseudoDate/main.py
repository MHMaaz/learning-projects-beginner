#in this project all months end after 30 days

def decide_order(date1, date2):
    if date1["Y"] == date2["Y"]:
        if date1["M"] < date2["M"]:
            return True # where true means that current date is less than other date
        else:
            return False # where false means that other date is smaller than current date
    elif date1["Y"] < date2["Y"]:
        return True
    elif date1["Y"] > date2["Y"]:
        return False

def get_pseudo_date(currentDict, otherDict):
    days = 0
    months = 0
    years = 0
    month_increment = 0
    day_increment = currentDict["D"]
    month_checker = currentDict["M"] # this will logically fix the incrementation of days AND months
    year_checker = currentDict["Y"]
    start_year = currentDict["Y"]
    end_year = int()
    
    while True:
        month_increment += 1
        day_increment += 1
        days += 1
        if day_increment == otherDict["D"]:
            if month_checker == otherDict["M"]:
                if year_checker == otherDict["Y"]:
                    end_year = year_checker
                    if days >= 360:
                        years = end_year - start_year
                    else:
                        years = 0
                    break
        
        if month_increment == 30:
            months += 1
            month_increment = 1
        
        if day_increment >= 30:
            day_increment = 1
            month_checker += 1
    
        if month_checker > 12:
            month_checker = 1
            year_checker += 1
            
    print(f"# Years : {years}\n# Months : {months}\n# Days : {days}")
def get_other_date(): # very similar to get_current_date()
    detectDivider = 0
    day = str()
    month = str()
    year = str()
    divider = str()
    date = input("Enter the other date upto which you want your \"Pseudo Date\" \"(DD/MM/YYYY)\" : ")
    for i in range(0, len(date)):
        if date[i].isdigit():
            if detectDivider == 0: # no divider has been detected
                day += date[i]
            elif detectDivider == 1:
                month += date[i]
            else:
                year += date[i]
        else: #non numeric value or a divider
            detectDivider += 1
            if divider != date[i]: # checking if there is no divider already in there
                divider += date[i]
    day = int(day)
    month = int(month)
    year = int(year)
    return { # returning as dict makes these values more accessible
        "D" : day,
        "M" : month,
        "Y" : year
    }

def get_current_date():
    detectDivider = 0
    day = str()
    month = str()
    year = str()
    divider = str()
    date = input("Enter your date \"(DD/MM/YYYY)\" : ")
    for i in range(0, len(date)):
        if date[i].isdigit():
            if detectDivider == 0: # no divider has been detected
                day += date[i]
            elif detectDivider == 1:
                month += date[i]
            else:
                year += date[i]
        else: #non numeric value or a divider
            detectDivider += 1
            if divider != date[i]: # checking if there is no divider already in there
                divider += date[i]
    day = int(day)
    month = int(month)
    year = int(year)
    return { # returning as dict makes these values more accessible
        "D" : day,
        "M" : month,
        "Y" : year,
        "div" : divider
    }
def main():
    current_date = get_current_date()
    other_date = get_other_date()
    order = decide_order(current_date, other_date)
    style = [current_date["div"]] * 11
    
    print(" ".join(style))
    if order is True: # true signifies big other_date
        get_pseudo_date(current_date, other_date)
    elif order is False: # false signifies big current_date
        get_pseudo_date(other_date, current_date)
    print(" ".join(style))
    
if __name__ == "__main__":
    main()