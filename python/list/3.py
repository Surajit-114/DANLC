def find_duplicate(values):
    duplicates = []
    for i in range(len(values) - 1):
        for j in range(i + 1, len(values)):
            if values[j] == values[i]:
                if values[j] not in duplicates:
                    duplicates.append(values[j])
    return duplicates


def main():
    values = [1, 2, 2, 4, 5, 2, 5, 3, 1]
    duplicates = find_duplicate(values)
    print("Duplicate values are:", end=" ")
    print(*duplicates, sep=", ")


if __name__ == "__main__":
    main()
