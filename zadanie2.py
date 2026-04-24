from datetime import date

DAYS_RU = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]

DIGIT_PATTERNS = {
    '0': ["***", "* *", "* *", "* *", "***"],
    '1': [" * ", "** ", " * ", " * ", "***"],
    '2': ["***", "  *", "***", "*  ", "***"],
    '3': ["***", "  *", "***", "  *", "***"],
    '4': ["* *", "* *", "***", "  *", "  *"],
    '5': ["***", "*  ", "***", "  *", "***"],
    '6': ["***", "*  ", "***", "* *", "***"],
    '7': ["***", "  *", "  *", "  *", "  *"],
    '8': ["***", "* *", "***", "* *", "***"],
    '9': ["***", "* *", "***", "  *", "***"],
}

def get_day_of_week(birth_date):
    return DAYS_RU[birth_date.weekday()]

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

def print_date_as_digits(birth_date):
    dd = f"{birth_date.day:02d}"
    mm = f"{birth_date.month:02d}"
    yyyy = str(birth_date.year)
    parts = list(dd) + [" "] + list(mm) + [" "] + list(yyyy)

    for row in range(5):
        line = ""
        for ch in parts:
            if ch == " ":
                line += "  "
            else:
                line += DIGIT_PATTERNS[ch][row] + " "
        print(line)

def main():
    print("Введите вашу дату рождения:")
    day   = int(input("День (1-31): "))
    month = int(input("Месяц (1-12): "))
    year  = int(input("Год (например, 1995): "))

    birth_date = date(year, month, day)

    print(f"\nДень недели рождения: {get_day_of_week(birth_date)}")
    print(f"Високосный год: {'да' if is_leap_year(year) else 'нет'}")
    print(f"Возраст: {get_age(birth_date)} лет")
    print("\nВаша дата рождения на табло:")
    print_date_as_digits(birth_date)

main()
