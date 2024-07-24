import logging

# configure logging
logging.basicConfig(
    filename="exceptions.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def read_and_log(filepath):
    try:
        with open(filepath, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError as err:
        logging.error(err)
        raise FileNotFoundError(err)
    except PermissionError as err:
        logging.error(f"Access denied: {err}")
        raise PermissionError(err)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise Exception(e)


def main():
    filepath = input("Enter a file path: ")
    try:
        read_and_log(filepath)
    except (FileNotFoundError, PermissionError) as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
