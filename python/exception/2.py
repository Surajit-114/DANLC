class OutOfRangeError(Exception):
    def __init__(self, message):
        super().__init__(message)

def main():
    try:
        num = int(input("Enter a number: "))
        if 0 <= num >= 100:
            raise OutOfRangeError("Please enter a number in 0 to 100 range!!!")
        else:
            print(f"Your entered number is: {num}")
    except OutOfRangeError as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()
