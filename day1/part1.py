if __name__ == '__main__':
    values_of_column1: list[int] = []
    values_of_column2: list[int] = []

    for line in open("./input.txt", "r"):
        temp_line: list[str] = line.split()
        values_of_column1.append(int(temp_line[0]))
        values_of_column2.append(int(temp_line[1]))

    values_of_column1.sort()
    values_of_column2.sort()

    total_distance: int = 0

    for val_of_col1, val_of_col2 in zip(values_of_column1, values_of_column2):
        total_distance += abs(val_of_col1 - val_of_col2)

    print(total_distance)