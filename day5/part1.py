def get_parsed_order(_line: str) -> tuple[int, int]:
    start_order: int = int(_line.split("|")[0])
    end_order: int = int(_line.split("|")[1])

    return start_order, end_order


def get_parsed_line(_line: str) -> tuple[int, ...]:
    return tuple(map(lambda num: int(num), _line.split(",")))



def get_required_orders(_pages: tuple[int, ...], _all_orders) -> list[tuple]:
    _result: list[tuple] = []

    for _order in _all_orders:
        are_required_contained: bool = all(num in _pages for num in _order)

        if are_required_contained:
            _result.append(_order)

    return _result


if __name__ == '__main__':
    with open("./input.txt", "r") as file:
        all_lines: list[str] = file.readlines()

    all_orders: list[tuple] = []
    all_pages_lines: list[tuple] = []
    result: int = 0

    for line in all_lines:
        if "|" in line:
            all_orders.append(get_parsed_order(line))

        elif "," in line:
            all_pages_lines.append(get_parsed_line(line))


    for pages_line in all_pages_lines:
        required_orders: list[tuple] = get_required_orders(pages_line, all_orders)
        pages_in_right_order: bool = True

        for order in required_orders:
            if pages_line.index(order[0]) > pages_line.index(order[1]):
                pages_in_right_order = False
                break

        if pages_in_right_order:
            result += pages_line[(len(pages_line) - 1) // 2]

    print(result)