if __name__ == '__main__':
    with open("./input.txt", "r") as file:
        all_lines: list[str] = file.readlines()

    counter: int = 0

    for row in range(1, len(all_lines) - 1):

        for center in range(1, len(all_lines[0]) - 2):
            diagonal_left: str = (all_lines[row - 1][center - 1] +
                                      all_lines[row][center] +
                                      all_lines[row + 1][center + 1])
            diagonal_right: str = (all_lines[row + 1][center - 1] +
                                         all_lines[row][center] +
                                         all_lines[row - 1][center + 1])

            if (diagonal_left == "MAS" or diagonal_left == "SAM") and \
                (diagonal_right == "MAS" or diagonal_right == "SAM"):
                counter += 1

    print(counter)
