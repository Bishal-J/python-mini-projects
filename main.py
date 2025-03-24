from calculator import run_calculator
from leap_year import  run_leap_year

start_app = True

app_list = {
    1: "Calculator",
    2: "Leap Year"
}

print("===MINI PROJECTS===")

while start_app:
    print("Mini Project List")
    for key in app_list:
        print(f"{key}. {app_list[key]}")

    app_num = int(input("Choose the app number e.g. 3: "))

    if app_num == 1:
        run_calculator()
    elif app_num == 2:
        run_leap_year()
    flag = input("Do you like to try other program. (Y/N) ").lower()

    if flag != 'y':
        start_app = False