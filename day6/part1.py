def get_guard_position(_map: list[str]) -> tuple[int, int]:
    for _index, _row in enumerate(_map):
        if "^" in _row:
            return _index, _row.index("^")


def mark_guard_position_in_row(_row: int, _pos: int):
    _row_breakdown: list[str] = [val for val in lab_map[_row]]
    _row_breakdown[_pos] = "X"
    lab_map[_row] = "".join(_row_breakdown)


def is_there_an_obstruction(_row_pos: int, _col_pos) -> bool:
    return True if lab_map[_row_pos][_col_pos] == "#" else False


def has_guard_left() -> bool:
    if guard_position[0] >= len(lab_map) - 1:
        return True
    if guard_position[0] == 0:
        return True
    if guard_position[1] == len(lab_map[0]) - 1:
        return True
    if guard_position[1] == 0:
        return True

    return False


if __name__ == '__main__':
    with open("./input.txt", "r") as file:
        lab_map: list[str] = [line.strip("\n") for line in file.readlines()]

    guard_position: tuple[int, int] = get_guard_position(lab_map)
    guard_direction: str = "up"
    result: int = 0

    while True:
        if has_guard_left():
            break

        mark_guard_position_in_row(guard_position[0], guard_position[1])

        match guard_direction:
            case "up":
                if not is_there_an_obstruction(guard_position[0] - 1, guard_position[1]):
                    guard_position = guard_position[0] - 1, guard_position[1]
                    mark_guard_position_in_row(guard_position[0], guard_position[1])
                else:
                    guard_direction = "right"

            case "right":
                if not is_there_an_obstruction(guard_position[0], guard_position[1] + 1):
                    guard_position = guard_position[0], guard_position[1] + 1
                    mark_guard_position_in_row(guard_position[0], guard_position[1])
                else:
                    guard_direction = "down"

            case "down":
                if not is_there_an_obstruction(guard_position[0] + 1, guard_position[1]):
                    guard_position = guard_position[0] + 1, guard_position[1]
                    mark_guard_position_in_row(guard_position[0], guard_position[1])
                else:
                    guard_direction = "left"

            case "left":
                if not is_there_an_obstruction(guard_position[0], guard_position[1] - 1):
                    guard_position = guard_position[0], guard_position[1] - 1
                    mark_guard_position_in_row(guard_position[0], guard_position[1])
                else:
                    guard_direction = "up"

    for row in lab_map:
        result += row.count("X")

    print(result)