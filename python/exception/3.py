def main():
    filepath = input("Enter file path: ")
    try:
        file = open(filepath, "r")
        content = file.read()
        print(content)
        file.close()
    except FileNotFoundError as err:
        print(err)


if __name__ == "__main__":
    main()
