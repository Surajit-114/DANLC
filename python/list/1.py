def list_sum(num_list):
    total = 0
    for num in num_list:
        total += num
    return total


def main():
    num_list = [1, 2, 3, 4, 5]
    total = list_sum(num_list)
    print(f"Sum of elements is: {total}")


if __name__ == "__main__":
    main()
