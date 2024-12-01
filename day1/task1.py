if __name__ == '__main__':
    values_of_column1: list[int] = []
    values_of_column2: list[int] = []

    for line in open("./input1.txt", "r"):
        temp_line: list[str] = line.split()
        values_of_column1.append(int(temp_line[0]))
        values_of_column2.append(int(temp_line[1]))

    values_of_column1.sort()
    values_of_column2.sort()

    total_distance: int = 0

    for index, value_of_column1 in enumerate(values_of_column1):
        total_distance += (abs(value_of_column1 - values_of_column2[index]))

    print(total_distance)