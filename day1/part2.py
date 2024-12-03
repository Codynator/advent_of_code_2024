if __name__ == '__main__':
    values_of_column1: list[int] = []
    values_of_column2: list[int] = []

    for line in open("./input.txt", "r"):
        temp_line: list[str] = line.split()
        values_of_column1.append(int(temp_line[0]))
        values_of_column2.append(int(temp_line[1]))

    score: int = 0

    for value_of_column1 in values_of_column1:
        score += value_of_column1 * values_of_column2.count(value_of_column1)

    print(score)