def main():
    colors = ["red", "green", "white", "black"]
    len_of_colors = len(colors)
    for idx in range(len_of_colors):
        last_index = len_of_colors - 1
        reverse_index = last_index - idx
        print(f"Index: {reverse_index}, Color: {colors[reverse_index]}")


if __name__ == "__main__":
    main()
