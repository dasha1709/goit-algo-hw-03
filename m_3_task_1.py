from datetime import datetime

def get_days_from_today(date):
    while True:
        try:
            date_object = datetime.strptime(date, "%Y-%m-%d")
            break
        except:
            print("Дані вказано не коректно!")
            date = input("Введірь дату (рік-місяць-день): ")

    current_date = datetime.today()
    difference = date_object - current_date
    return difference.days

date = input("Введірь дату (рік-місяць-день): ")

print(get_days_from_today(date))