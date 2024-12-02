def lines_generator():
    for line in open("./input1.txt", "r"):
        yield line


def is_report_safe(_report: list[int]) -> bool:
    is_increasing: bool = _report[0] < _report[1]

    for i in range(len(_report) - 1):
        difference: int = _report[i] - _report[i + 1]
        is_pair_increasing: bool = difference < 0

        if difference == 0:
            return False
        if is_pair_increasing != is_increasing:
            return False
        if abs(difference) > 3:
            return False

    return True


if __name__ == '__main__':
    all_lines = lines_generator()
    counter: int = 0

    for report in all_lines:
        parsed_report: list[int] = [int(num) for num in report.split()]

        if is_report_safe(parsed_report):
            counter += 1
            continue

        # Brute forced it because I don't know how to solve it like a normal human being.
        for index, _ in enumerate(parsed_report):
            copy_parsed_report: list[int] = parsed_report.copy()
            copy_parsed_report.pop(index)

            if is_report_safe(copy_parsed_report):
                counter += 1
                break

    print(counter)