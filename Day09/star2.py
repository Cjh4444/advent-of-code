def decompress_string(string):
    empty_block = False
    decompressed_string = []

    count = 0

    for num in string:
        if empty_block:
            decompressed_string.extend(["."] * int(num))
        else:
            decompressed_string.extend([str(count)] * int(num))
            count += 1
        empty_block = not empty_block

    return decompressed_string


def defragment_disk(disk):

    file_end_pointer = len(disk) - 1
    file_start_pointer = file_end_pointer

    while file_end_pointer > len(disk) // 2:
        while disk[file_end_pointer] == ".":
            file_end_pointer -= 1

        file_start_pointer = file_end_pointer

        fragment_length = 0
        while disk[file_end_pointer] == disk[file_start_pointer]:
            file_start_pointer -= 1
            fragment_length += 1

        file_start_pointer += 1

        for i in range(file_end_pointer - fragment_length):
            if all(x == "." for x in disk[i : i + fragment_length]):
                for space in range(i):
                    print(f"{file_start_pointer} {file_end_pointer} {space}")
                    disk[i + space], disk[file_start_pointer + space] = (
                        disk[file_start_pointer + space],
                        disk[i + space],
                    )
                print("".join(disk))
            break
        file_start_pointer -= 1
        file_end_pointer = file_start_pointer - 1


def calculate_checksum(disk):
    checksum = 0
    for mult, num in enumerate(disk):
        if num == ".":
            break
        checksum += mult * int(num)

    return checksum


with open("test.txt") as f:
    line = f.readline().strip()

    disk = decompress_string(line)
    print("".join(disk))
    defragment_disk(disk)

    print("".join(disk))

    # print(calculate_checksum(disk))
