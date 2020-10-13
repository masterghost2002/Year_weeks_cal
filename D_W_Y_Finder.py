####### Days weeks year finder 11/10/2020
def counter(days):
    if days >= 365:
        if days % 365 == 0:
            years = days / 365
            print(f"Number of Years: {years}")
        elif days % 365 != 0:
            r_days = days % 365
            r_days_week = days - r_days
            n_years = r_days_week / 365
            if r_days_week % 7 == 0:
                weeks = r_days_week / 7
                print(f"Number of Years        : {n_years}")
                print(f"Number of Weeks        : {weeks}")
                print("Number of Remaining Days: 0")
            elif r_days_week % 7 != 0:
                n_r_days = r_days_week % 7
                days_week = r_days_week - n_r_days
                n_weeks = days_week / 7
                print(f"Number of Years         : {n_years}")
                print(f"Number of Weeks         : {n_weeks}")
                print(f"Number of Remaining Days: {n_r_days}")
    elif days < 365:
        if days % 7 == 0:
            weeks = days / 7
            print("Number of Years         : 0")
            print(f"Number of Weeks        : {weeks}")
            print("Number of Remaining Days: 0")
        elif days % 7 != 0:
            r_days = days % 7
            r_days_week = days - r_days
            n_weeks = r_days_week / 7
            print("Number of Years          : 0")
            print(f"Number of weeks          : {n_weeks}")
            print(f"Number of Remaining Days: {r_days}")
if __name__ == '__main__':
    days = int(input("Enter Days Here\n"))
    counter(days)
