def split_list(values, split_index):
    first_part = values[:split_index]
    last_part = values[split_index:]
    return first_part, last_part


def main():
    first_part_len = int(input("Enter first part length: "))
    values = [1, 1, 2, 3, 4, 4, 5, 1]
    first_part, last_part = split_list(values, first_part_len)
    print("First part of the list: ", first_part)
    print("Last part of the list: ", last_part)


if __name__ == "__main__":
    main()
