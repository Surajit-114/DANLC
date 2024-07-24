def is_numerical(value):
    try:
        a = float(value)
        return True
    except ValueError:
        return False


def get_number():
    value = input("Enter a value: ")

    if is_numerical(value):
        return float(value)
    else:
        raise TypeError("Please enter a numerical value!!!")


def main():
    try:
        value1 = get_number()
        value2 = get_number()

        print(f"Your entered numbers are : {value1}, {value2}")
    except TypeError as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()
