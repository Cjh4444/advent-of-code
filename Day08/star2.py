import math


def distance(p1, p2):
    return math.sqrt(
        math.pow(p1[0] - p2[0], 2)
        + math.pow(p1[1] - p2[1], 2)
        + math.pow(p1[2] - p2[2], 2)
    )


def pre_calc_distances(points):
    distances = {}
    for p1 in points:
        for p2 in points:
            if p1 == p2 or distances.get((min(p1, p2), max(p1, p2)), False):
                continue

            distances[(min(p1, p2), max(p1, p2))] = distance(p1, p2)

    return distances


def clusters_shortest_n(distances: dict[tuple[tuple, tuple], int], n):
    clusters: list[set] = []
    added_points = set()

    smallest_pair = None

    while len(added_points) != n:
        smallest_pair = min(distances, key=distances.get)

        distances.pop(smallest_pair)

        _ = smallest_pair[0] in added_points
        __ = smallest_pair[1] in added_points

        first_cluster = None
        second_cluster = None

        if _:
            for cluster in clusters:
                if smallest_pair[0] in cluster:
                    first_cluster = cluster

        if __:
            for cluster in clusters:
                if smallest_pair[1] in cluster:
                    second_cluster = cluster

        if _ and __:
            # merge clusters case
            if first_cluster == second_cluster:
                continue
            clusters.remove(second_cluster)
            first_cluster.update(second_cluster)
        elif _ or __:
            if _:
                first_cluster.add(smallest_pair[1])
                added_points.add(smallest_pair[1])
            else:
                second_cluster.add(smallest_pair[0])
                added_points.add(smallest_pair[0])
        else:
            added_points.add(smallest_pair[0])
            added_points.add(smallest_pair[1])
            new_cluster = set()
            new_cluster.add(smallest_pair[0])
            new_cluster.add(smallest_pair[1])

            clusters.append(new_cluster)

        print(len(added_points))

    return clusters, smallest_pair


def process(file):
    with open(file) as f:
        points = [tuple(map(int, line.split(","))) for line in f]
        n = len(points)

        distances = pre_calc_distances(points)

        clusters, final_pair = clusters_shortest_n(distances, n)

        result = final_pair[0][0] * final_pair[1][0]
        print(result)
        return result


assert process("test.txt") == 25272
process("data.txt")
