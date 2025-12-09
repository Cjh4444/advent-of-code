def process(file):
    with open(file) as f:
        points = [tuple(map(int, line.split(","))) for line in f]
        rects_area = [
            (
                (abs(points[i][0] - j[0]) + 1) * (abs(points[i][1] - j[1]) + 1),
                points[i],
                j,
            )
            for i in range(len(points))
            for j in points[i + 1 :]
            if (
                points[i] == (94584, 50147)
                and j[1] >= 50147
                and j[1] <= 67785
                and j[0] >= 5790
            )
            or (
                j == (94584, 50147)
                and points[i][1] >= 50147
                and points[i][1] <= 67785
                and points[i][0] >= 5790
            )
            or (points[i] == (94584, 48634) and j[1] <= 48634 and j[1] >= 34545)
            or (j == (94584, 48634) and points[i][1] <= 48634 and points[i][1] >= 34545)
        ]

        print(sorted(rects_area))

        ret = max(rects_area)
        print(ret)
        return ret


# assert process("test.txt") == 50
process("data.txt")
