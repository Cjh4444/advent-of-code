def process(file):
    with open(file) as f:
        points = [tuple(map(int, line.split(","))) for line in f]
        rects_area = [
            (abs(points[i][0] - j[0]) + 1) * (abs(points[i][1] - j[1]) + 1)
            for i in range(len(points))
            for j in points[i + 1 :]
        ]

        ret = max(rects_area)
        print(ret)
        return ret


assert process("test.txt") == 50
process("data.txt")
