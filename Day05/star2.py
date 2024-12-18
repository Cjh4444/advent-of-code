pages_after_page: dict[int, set[int]] = {}
pages_before_page: dict[int, set[int]] = {}
mid_page_sum = 0


def sort_incorrect_order(order: list):
    correct_order = [order[0]]
    for page in order[1:]:
        for idx, correct_page in enumerate(correct_order):
            if page in pages_after_page[correct_page]:
                if idx < len(correct_order) - 1:
                    continue
                correct_order.insert(idx + 1, page)
                break
            elif page in pages_before_page[correct_page]:
                correct_order.insert(idx, page)
                break

    return correct_order


with open("data.txt") as f:
    rules_done = False
    for line in f:
        if line == "\n":
            rules_done = True
            continue

        if not rules_done:
            before, after = line.split("|")
            before, after = int(before), int(after)

            pages_after_page.setdefault(before, set()).add(after)
            pages_before_page.setdefault(after, set()).add(before)
        else:
            order = [int(x) for x in line.strip().split(",")]

            is_valid = True

            for idx, page in enumerate(order):
                before = order[:idx]
                after = order[idx + 1 :]

                for before_page in before:
                    if before_page in pages_after_page.setdefault(page, set()):
                        is_valid = False
                        break
                for after_page in after:
                    if after_page in pages_before_page.setdefault(page, set()):
                        is_valid = False
                        break
            if not is_valid:
                # print(f"{pages_after_page}")
                # print(f"{pages_before_page}")
                mid_page_sum += sort_incorrect_order(order)[
                    int(len(order) / 2)
                ]
            # print(is_valid)
    print(mid_page_sum)
    # print(after_dict)
    # print(before_dict)
