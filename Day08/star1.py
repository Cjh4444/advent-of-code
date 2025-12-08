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

    for i in range(n):
        smallest_pair = min(distances, key=distances.get)
        distances.pop(smallest_pair)

        pair1_in_cluster = smallest_pair[0] in added_points
        pair2_in_cluster = smallest_pair[1] in added_points

        first_cluster = None
        second_cluster = None

        if pair1_in_cluster:
            for cluster in clusters:
                if smallest_pair[0] in cluster:
                    first_cluster = cluster

        if pair2_in_cluster:
            for cluster in clusters:
                if smallest_pair[1] in cluster:
                    second_cluster = cluster

        if pair1_in_cluster and pair2_in_cluster:
            if first_cluster == second_cluster:
                continue
            clusters.remove(second_cluster)
            first_cluster.update(second_cluster)
        elif pair1_in_cluster or pair2_in_cluster:
            if pair1_in_cluster:
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

    return clusters


def process(file, n):
    with open(file) as f:
        points = [tuple(map(int, line.split(","))) for line in f]
        distances = pre_calc_distances(points)
        clusters = clusters_shortest_n(distances, n)
        clusters.sort(reverse=True, key=len)

        result = len(clusters[0]) * len(clusters[1]) * len(clusters[2])
        print(result)

        return result


assert process("test.txt", 10) == 40
process("data.txt", 1000)
