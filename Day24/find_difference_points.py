correct = "1101010110100010011011110000111100011011100110"
actual = "1101010110110010011100010010000000011011100110"
length = len(correct) - 1



for z_num, (c, a) in enumerate(zip(correct, actual)):
    if c != a:
        print(f"z{length - z_num} is {a}, should be {c}")
    # else:
    #     print(f"z{length - z_num}")