def decompress_string(string):
    empty_block = False
    decompressed_string = []

    count = 0

    for num in string:
        if empty_block:
            if num != "0":
                decompressed_string.append(["."] * int(num))
        else:
            if num != "0":
                decompressed_string.append([str(count)] * int(num))
                count += 1
        empty_block = not empty_block

    return decompressed_string


def print_disk(disk):
    for i in disk:
        print("".join(i), end="")
    print()


def defragment_disk(disk: list[list]):
    curr_file_idx = len(disk) - 1

    while curr_file_idx > 0:
        # print(curr_file_idx)
        if disk[curr_file_idx][0] == ".":
            curr_file_idx -= 1
            continue
        # print(disk[curr_file_idx])
        for idx, space in enumerate(disk[:curr_file_idx]):
            if space[0] == ".":
                if len(space) >= len(disk[curr_file_idx]):
                    if len(space) == len(disk[curr_file_idx]):
                        disk[idx], disk[curr_file_idx] = (
                            disk[curr_file_idx],
                            disk[idx],
                        )
                    else:
                        fragment_space, extra_space = (
                            space[0 : len(disk[curr_file_idx])],
                            space[len(disk[curr_file_idx]) :],
                        )
                        disk.pop(idx)
                        disk.insert(idx, extra_space)
                        disk.insert(idx, fragment_space)
                        curr_file_idx += 1

                        # print(f"disk[idx] is {disk[idx]}")
                        # print(f"disk[curr_file_idx] is {disk[curr_file_idx]}")

                        disk[idx], disk[curr_file_idx] = (
                            disk[curr_file_idx],
                            disk[idx],
                        )
                        if idx + 2 < len(disk):
                            # print(f"disk[idx + 2] is {disk[idx+2]}")
                            if disk[idx + 2][0] == ".":
                                disk[idx + 1].extend(disk[idx + 2])
                                disk.pop(idx + 2)
                    break
        # print_disk(disk)
        curr_file_idx -= 1


def flatten(disk):
    while len(disk) > 1:
        disk[0].extend(disk.pop(1))


def calculate_checksum(disk):
    checksum = 0
    for mult, num in enumerate(disk):
        if num == ".":
            continue
        checksum += mult * int(num)

    return checksum


with open("data.txt") as f:
    line = f.readline().strip()

    disk = decompress_string(line)
    # print_disk(disk)
    defragment_disk(disk)
    # print_disk(disk)

    # print(disk)
    flatten(disk)
    disk = disk[0]
    # print(disk)

    print(calculate_checksum(disk))
