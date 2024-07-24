def find_min(num_list):
    minimum = num_list[0]
    for num in num_list:
        if num < minimum:
            minimum = num
    return minimum


def find_max(num_list):
    maximum = num_list[0]
    for num in num_list:
        if num > maximum:
            maximum = num
    return maximum


def main():
    num_list = [1, 2, 3, 4, 5, 7, 8]
    minimum = find_min(num_list)
    maximum = find_max(num_list)
    print(f"Minimum number is: {minimum}")
    print(f"Maximum number is: {maximum}")


if __name__ == "__main__":
    main()
