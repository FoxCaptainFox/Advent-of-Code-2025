from utils import read_data
import math
from collections import Counter

# Part 1

DISTANCES_NUM_TO_CONSIDER = 1000
BIGGEST_CLUSTER_NUM_TO_MULTIPLY = 3

points = [[int(x) for x in line.split(",")] for line in read_data(8)]

distances = dict()
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances[(i, j)] = math.dist(points[i], points[j])

point_pairs_sorted_by_distance = [k for k, _ in sorted(distances.items(), key=lambda item: item[1])]

cluster_ids_by_point = list(range(len(points)))

for point_1, point_2 in point_pairs_sorted_by_distance[:DISTANCES_NUM_TO_CONSIDER]:
    cluster_id_1, cluster_id_2 = cluster_ids_by_point[point_1], cluster_ids_by_point[point_2]
    if cluster_id_1 != cluster_id_2:
        cluster_ids_by_point[:] = [cluster_id_1 if id == cluster_id_2 else id for id in cluster_ids_by_point]

id_counter = Counter(cluster_ids_by_point)
result = math.prod(sorted(id_counter.values())[-BIGGEST_CLUSTER_NUM_TO_MULTIPLY:])
print(result)


# Part 2

COORDINATE_INDEX_TO_MULTIPLY = 0

points = [[int(x) for x in line.split(",")] for line in read_data(8)]

distances = dict()
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distances[(i, j)] = math.dist(points[i], points[j])

point_pairs_sorted_by_distance = [k for k, _ in sorted(distances.items(), key=lambda item: item[1])]

cluster_ids_by_point = list(range(len(points)))

for point_1, point_2 in point_pairs_sorted_by_distance:
    cluster_id_1, cluster_id_2 = cluster_ids_by_point[point_1], cluster_ids_by_point[point_2]
    if cluster_id_1 != cluster_id_2:
        cluster_ids_by_point[:] = [cluster_id_1 if id == cluster_id_2 else id for id in cluster_ids_by_point]
        if len(set(cluster_ids_by_point)) == 1:
            print(points[point_1][COORDINATE_INDEX_TO_MULTIPLY] * points[point_2][COORDINATE_INDEX_TO_MULTIPLY])
            break
