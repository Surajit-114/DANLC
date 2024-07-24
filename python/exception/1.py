try:
    dividend = float(input("Enter dividend: "))
    divisor = float(input("Enter divisor: "))

    divison = dividend / divisor
    print(f"Divison is: {divison}")
except ZeroDivisionError as err:
    print(f"Error: {err}")
