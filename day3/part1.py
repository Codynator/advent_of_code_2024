from re import findall


def get_input_values(str_func: str) -> tuple[int, int]:
    unparsed_values: list[str] = findall(r"[0-9]+", str_func)
    return int(unparsed_values[0]), int(unparsed_values[1])


def get_sum_of_line(_line: list[str]) -> int:
    _sum: int = 0

    for _func in _line:
        values: tuple[int, int] = get_input_values(_func)
        _sum += values[0] * values[1]

    return _sum


if __name__ == '__main__':
    sum_of_functions: int = 0

    for line in open("input.txt", "r"):
        new_line: list[str] = findall(r"mul\([0-9]+,[0-9]+\)", line)
        sum_of_functions += get_sum_of_line(new_line)

    print(sum_of_functions)