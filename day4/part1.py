def clean_line(_line: str) -> str:
    _cleaned_line: str = ""

    for _char in _line:
        if _char in "XMAS":
            _cleaned_line += _char
        else:
            _cleaned_line += "_"

    return _cleaned_line


def count_in_list(data: list[str], searched_for: str) -> int:
    counter: int = 0
    for val in data:
        counter += val.count(searched_for) + val[::-1].count(searched_for)

    return counter


if __name__ == '__main__':
    with open("./input.txt", "r") as file:
        raw_all_lines: list[str] = file.readlines()

    cleaned_rows: list[str] = []
    cleaned_cols: list[str] = []
    cleaned_diagonals_left_right: list[str] = []
    cleaned_diagonals_right_left: list[str] = []

    for row in raw_all_lines:
        cleaned_rows.append(clean_line(row))

    for col in range(len(cleaned_rows[0]) - 1):
        full_col: str = ""

        for row in range(len(cleaned_rows)):
            full_col += cleaned_rows[row][col]

        cleaned_cols.append(full_col)

    for i in range(len(cleaned_cols) * 2):
        full_diagonal: str = ""

        for j in range(i + 1):
            try:
                full_diagonal += cleaned_rows[j][i - j]
            except IndexError:
                continue

        if len(full_diagonal) >= 4:
            cleaned_diagonals_left_right.append(full_diagonal)

    for i in range(len(cleaned_cols) * 2):
        full_diagonal: str = ""

        for j in range(i + 1):
            try:
                _row = len(cleaned_rows) - 1 - j
                _col = i - j

                if _row >= 0 and _col >= 0:
                    full_diagonal += cleaned_rows[_row][_col]

            except IndexError:
                continue

        if len(full_diagonal) >= 4:
            cleaned_diagonals_right_left.append(full_diagonal)

    result: int = count_in_list(cleaned_rows, "XMAS")
    result += count_in_list(cleaned_cols, "XMAS")
    result += count_in_list(cleaned_diagonals_left_right, "XMAS")
    result += count_in_list(cleaned_diagonals_right_left, "XMAS")
    print(result)
