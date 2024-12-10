after_dict: dict[int, set[int]] = {}
before_dict: dict[int, set[int]] = {}
mid_page_sum = 0

with open("data.txt") as f:
    rules_done = False
    for line in f:
        if line == "\n":
            rules_done = True
            continue

        if not rules_done:
            before, after = line.split("|")
            before, after = int(before), int(after)

            after_dict.setdefault(before, set()).add(after)
            before_dict.setdefault(after, set()).add(before)
        else:
            order = [int(x) for x in line.strip().split(",")]

            is_valid = True

            for idx, page in enumerate(order):
                before = order[:idx]
                after = order[idx + 1 :]

                for before_page in before:
                    if before_page in after_dict.setdefault(page, set()):
                        is_valid = False
                        break
                for after_page in after:
                    if after_page in before_dict.setdefault(page, set()):
                        is_valid = False
                        break
            if is_valid:
                mid_page_sum += order[int(len(order) / 2)]
            # print(is_valid)
    print(mid_page_sum)
    # print(after_dict)
    # print(before_dict)
