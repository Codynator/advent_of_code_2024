from re import findall


def get_input_values(str_func: str) -> tuple[int, int]:
    unparsed_values: list[str] = findall(r"[0-9]+", str_func)
    return int(unparsed_values[0]), int(unparsed_values[1])


def get_sum_of_line(_line: list[str]) -> int:
    _sum: int = 0
    _stop: bool = False

    for _func in _line:
        if _func == "don't()":
            _stop = True
            continue

        if _func == "do()":
            _stop = False
            continue

        if _stop:
            continue

        values: tuple[int, int] = get_input_values(_func)
        _sum += values[0] * values[1]

    return _sum


if __name__ == '__main__':
    sum_of_functions: int = 0
    flatten_line: list[str] = []

    for line in open("input.txt", "r"):
        new_line: list[str] = findall(r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", line)

        for raw_func in new_line:
            flatten_line.append(raw_func)

    sum_of_functions = get_sum_of_line(flatten_line)
    print(sum_of_functions)