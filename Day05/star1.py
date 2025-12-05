def process(file):
    with open(file) as f:
        fresh_ingredients: set = set()
        for line in f:
            if line == "\n":
                break

            start, end = list(map(int, line.split("-")))

            fresh_ingredients.add(range(start, end + 1))

        return sum(
            [
                any(
                    [
                        int(line) in ingredient_range
                        for ingredient_range in fresh_ingredients
                    ]
                )
                for line in f
            ]
        )


assert process("test.txt") == 3
print(process("data.txt"))
