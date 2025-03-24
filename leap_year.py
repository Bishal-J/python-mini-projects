def run_leap_year():
    def is_leap_year(year):
        """Check if a year is a leap year."""
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    is_running = True

    while is_running:
        user_input = input("Enter a year to check if it's a leap year: ")

        if user_input.isdigit():
            year = int(user_input)
            if is_leap_year(year):
                print(f"Year {year} is a Leap Year.")
            else:
                print(f"Year {year} is NOT a Leap Year.")
        else:
            print("Please enter a valid positive integer.")

        user_choice = input("Check another year? (Y/N): ").lower()
        if user_choice != 'y':
            is_running = False

    print("Goodbye!")