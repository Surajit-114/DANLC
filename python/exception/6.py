import datetime

class InvalidDateValueError(Exception):
    def __init__(self, message):
        super().__init__(message)


def check_date(year, month, day):
    # checking month validity
    if 1 <= month >= 12:
        raise InvalidDateValueError("Error: month must be between 1 to 12")

    # checking date validity
    if month in [1, 3, 5, 7, 8, 10, 12]:  # 31 days
        if not (1 <= day <= 31):
            raise InvalidDateValueError(f"In month {month}, There should be 31 days!!")
    elif month in [4, 6, 9, 11]:  # 30 days
        if not (1 <= day <= 30):
            raise InvalidDateValueError(f"In month {month}, There should be 30 days!!")
    elif month == 2:  # February month
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if not (1 <= day <= 29):
                raise InvalidDateValueError(
                    f"In month {month}, There should be 29 days as it is a leap year!!"
                )
        elif not (1 <= day <= 28):
            raise InvalidDateValueError(
                f"In month {month}, There should be 28 days as it is not a leap year!!"
            )


def get_valid_date():
    try:
        date = input("Enter a date: ")
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])

        check_date(year, month, day)

        return datetime.date(year, month, day).strftime("%Y-%m-%d")

    except ValueError:
        raise ValueError("Invalid date format!!")


def main():
    try:
        date = get_valid_date()
        print(f"Your entered date is: {date}")

    except (InvalidDateValueError, ValueError) as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()
