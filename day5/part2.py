from timeit import default_timer


def get_parsed_order(_line: str) -> tuple[int, int]:
    start_order: int = int(_line.split("|")[0])
    end_order: int = int(_line.split("|")[1])

    return start_order, end_order


def get_parsed_line(_line: str) -> tuple[int, ...]:
    return tuple(map(lambda num: int(num), _line.split(",")))


def get_required_orders(_pages: tuple[int, ...], _all_orders: list[tuple]) -> list[tuple]:
    _result: list[tuple] = []

    for _order in _all_orders:
        are_required_contained: bool = all(num in _pages for num in _order)

        if are_required_contained:
            _result.append(_order)

    return _result


def are_pages_ordered(_pages: tuple[int, ...] | list[int], _required_orders) -> bool:
    _pages_in_right_order: bool = True

    for _order in _required_orders:
        if _pages.index(_order[0]) > _pages.index(_order[1]):
            _pages_in_right_order = False
            break

    return _pages_in_right_order


def get_corrected_line(_pages: tuple[int, ...], _required_orders: list[tuple]) -> tuple[int, ...]:
    _pages = list(_pages)

    while not are_pages_ordered(_pages, _required_orders):
        for _order in _required_orders:
            start_page_index: int = _pages.index(_order[0])
            end_page_index: int = _pages.index(_order[1])

            if start_page_index > end_page_index:
                _pages[start_page_index], _pages[end_page_index] = _pages[end_page_index], _pages[start_page_index]

    return tuple(_pages)


if __name__ == '__main__':
    start_time = default_timer()

    with open("./input.txt", "r") as file:
        all_lines: list[str] = file.readlines()

    divider_index: int = all_lines.index("\n")

    all_orders: list[tuple] = []
    all_pages_lines: list[tuple] = []
    result: int = 0

    for order in all_lines[0:divider_index]:
        all_orders.append(get_parsed_order(order))

    for pages_line in all_lines[divider_index + 1: len(all_lines)]:
        all_pages_lines.append(get_parsed_line(pages_line))


    for pages_line in all_pages_lines:
        required_orders: list[tuple] = get_required_orders(pages_line, all_orders)
        pages_in_right_order: bool = True

        for order in required_orders:
            if pages_line.index(order[0]) > pages_line.index(order[1]):
                pages_in_right_order = False
                break

        if pages_in_right_order:
            continue

        corrected_pages_line: tuple[int, ...] = get_corrected_line(pages_line, required_orders)
        result += corrected_pages_line[len(corrected_pages_line) // 2]

    print(result)
    print(f"TIME: {default_timer() - start_time}")
