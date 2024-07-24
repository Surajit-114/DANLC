def parse_file(file_path):
    count = 1
    numlist = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                num = float(line.strip())
                numlist.append(num)
                count += 1
        return numlist

    except FileNotFoundError as err:
        raise FileNotFoundError(err)
    except PermissionError as err:
        raise PermissionError(err)
    except ValueError:
        raise ValueError(f"at line no. {count} non numeric data found!!")


def main():
    filePath = input("Enter a file path: ")
    try:
        nums = parse_file(filePath)
        print("Content of the file: ")
        print(*nums, sep=", ")
    except (FileNotFoundError, PermissionError, ValueError) as err:
        print(f"Error: {err}")


if __name__ == "__main__":
    main()
