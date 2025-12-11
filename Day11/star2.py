from functools import cache

graph: dict[str, list[str]] = {}


@cache
def traverse_graph(start, dest, passed_fft, passed_dac):
    if start == "svr":
        return 0

    if start == dest:
        # print(curr_path, end="")
        if passed_fft and passed_dac:
            # print(" yes")
            return 1
        # print(" no")
        return 0

    fft = passed_fft or start == "fft"
    dac = passed_dac or start == "dac"

    total = 0
    for server in graph[start]:
        total += traverse_graph(
            server,
            dest,
            fft,
            dac,
        )

    return total


def process(file):
    graph.clear()
    traverse_graph.cache_clear()

    with open(file) as f:
        for line in f:
            data = line.split()

            source = data[0][:-1]
            for dest in data[1:]:
                graph.setdefault(source, []).append(dest)

        print(
            ret := sum(
                traverse_graph(server, "out", False, False) for server in graph["svr"]
            )
        )

        return ret


assert process("test_star2.txt") == 2
process("data.txt")
