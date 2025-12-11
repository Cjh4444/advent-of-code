from collections import deque


def traverse_graph(graph):
    paths: deque[list[str]] = deque([[path] for path in graph["you"]])

    count = 0

    while paths:
        path = paths.pop()

        if path[-1] == "out":
            count += 1
            continue

        for dest in graph[path[-1]]:
            new_path = path[:]
            new_path.append(dest)
            paths.append(new_path)

    return count


def process(file):
    with open(file) as f:
        graph: dict[str, list[str]] = {}

        for line in f:
            data = line.split()

            source = data[0][:-1]
            for dest in data[1:]:
                graph.setdefault(source, []).append(dest)

        print(ret := traverse_graph(graph))
        return ret


assert process("test_star1.txt") == 5
process("data.txt")
