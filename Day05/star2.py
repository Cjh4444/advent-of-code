def add_range(ranges, start, end):
    # print(f"adding range ({start}, {end})")
    overlaps = False
    idx = 0
    for idx, item_range in enumerate(ranges):
        range_object = range(item_range[0], item_range[1] + 1)

        if start in range_object or end in range_object:
            # print(
            #     f"({start}, {end}) is contained in ({item_range[0]}, {item_range[1]})"
            # )
            overlaps = True
            break

    if overlaps:
        original_range = ranges.pop(idx)
        new_range = (min(original_range[0], start), max(original_range[1], end))
        # print(
        #     f"combined ({item_range[0]}, {item_range[1]}) and ({start}, {end}) to be ({new_range[0]}, {new_range[1]})"
        # )
        ranges.append(new_range)
    else:
        ranges.append((start, end))


def collapse_ranges(ranges):
    new_ranges = []

    for item_range in ranges:
        add_range(new_ranges, item_range[0], item_range[1])

    return new_ranges


def process(file):
    with open(file) as f:
        ranges: list[tuple[int, int]] = []

        for line in f:
            # print(f"working on {line}", end="")
            if line == "\n":
                break

            start, end = list(map(int, line.split("-")))

            add_range(ranges, start, end)
        ranges = sorted(ranges)

        ranges = collapse_ranges(ranges)

        return sum((item_range[1] - item_range[0] + 1) for item_range in ranges)


assert process("test.txt") == 14
print(process("data.txt"))
