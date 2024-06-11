from datetime import date

birth_day = int(input("Enter you birth day "))
birth_month = int(input("Enter your birth month "))
birth_year = int(input("Enter your birth year "))

current_day = date.today().day
current_month = date.today().month
current_year = date.today().year

ageDay = current_day-birth_day
ageMonth = current_month-birth_month
ageYear = current_year-birth_year

print(f"Your Age is {ageYear} years, {ageMonth} months, {ageDay} days")