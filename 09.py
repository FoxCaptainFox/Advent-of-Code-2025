from utils import read_data

def get_area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)


# Part 1

points = [[int(x) for x in row.split(",")] for row in read_data(9)]

max_area = 0

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        area = get_area(points[i], points[j])
        if max_area < area:
            max_area = area
print(max_area)


# Part 2
# Good luck reading this

def get_neighboring_undefined_cells(cell_x, cell_y, this_field):
    neighboring_cells = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    
    for dx, dy in directions:
        new_x, new_y = cell_x + dx, cell_y + dy
        if (0 <= new_x < len(this_field) 
            and 0 <= new_y < len(this_field[0]) 
            and this_field[new_x][new_y] is None):
            yield (new_x, new_y)


def check_if_rectangle_has_all_tiles_true(corner1, corner2, this_field):
    for tile_x in range(min(corner1[0], corner2[0]), max(corner1[0], corner2[0]) + 1):
        for tile_y in range(min(corner1[1], corner2[1]), max(corner1[1], corner2[1]) + 1):
            if not this_field[tile_x][tile_y]:
                return False
    return True

original_points = [[int(x) for x in row.split(",")] for row in read_data(9)]
original_xs = sorted(set([p[0] for p in original_points]))
original_ys = sorted(set([p[1] for p in original_points]))
# e.g., (1, 100), (10, 10), (100, 1) -> (0, 2), (1, 1), (2, 0)
compressed_points = [(original_xs.index(p[0]), original_ys.index(p[1])) for p in original_points]

# true = tile is red or green, false = empty, None = TBA
field = [[None]*len(original_ys) for _ in range(len(original_xs))]

for i in range(len(compressed_points)):
    line_start, line_end = compressed_points[i-1], compressed_points[i]
    for point_in_line_x in range(min(line_start[0], line_end[0]), max(line_start[0], line_end[0]) + 1):
        for point_in_line_y in range(min(line_start[1], line_end[1]), max(line_start[1], line_end[1]) + 1):
            field[point_in_line_x][point_in_line_y] = True

# add margin
field_with_margin = \
      [[None] * (len(original_ys) + 2)] \
    + [[None] + row + [None] for row in field] \
    + [[None] * (len(original_ys) + 2)]

# propagate empty cels
# the method doesn't account for cavities in the shape
tiles_to_mark_empty = set([(0,0)])

while tiles_to_mark_empty:
    new_tiles_to_mark_empty = set()
    for (tile_x, tile_y) in tiles_to_mark_empty:
        field_with_margin[tile_x][tile_y] = False
        foo = list(get_neighboring_undefined_cells(tile_x, tile_y, field_with_margin))
        new_tiles_to_mark_empty.update(get_neighboring_undefined_cells(tile_x, tile_y, field_with_margin))
    tiles_to_mark_empty = new_tiles_to_mark_empty

# remove margin and mark remaining undefined tiles as true
field = [[tile is None or tile for tile in line[1:-1]] for line in field_with_margin[1:-1]]

max_area = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        if not check_if_rectangle_has_all_tiles_true(compressed_points[i], compressed_points[j], field):
            continue
        area = get_area(original_points[i], original_points[j])
        if max_area < area:
            max_area = area
print(max_area)
