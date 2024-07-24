def safe_list_access(arr, index):
    try:
        return arr[index]
    except IndexError:
        raise IndexError("Error: Index out of range")
    except Exception as e:
        raise Exception(f"Error: {e}")


def main():
    try:
        testlists = [
            ([1, 2, 3, 4, 5], 2),
            ([1, 2, 3, 4, 5], -1),
            ([1, 2, 3, 4, 5], 10),
        ]
        for arr, idx in testlists:
            value = safe_list_access(arr, idx)
            print(f"Value at index {idx} is: {value}")
    except IndexError as err:
        print(err)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
