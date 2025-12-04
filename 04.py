from utils import read_data

EMPTY_CELL = "."
FILLED_CELL = "@"
MAX_FILLED_CELLS_AS_NEIGHBORS = 3

def get_neigbor_indexes(cell_i, cell_j, i_len, j_len):
    for i in range(cell_i - 1, cell_i + 2):
        for j in range(cell_j - 1, cell_j + 2):
            if i == cell_i and j == cell_j:
                continue
            if 0 <= i < i_len and 0 <= j < j_len:
                yield (i, j)


# Part 1

grid = read_data(4, True)
result_num = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != FILLED_CELL:
            continue
        filled_neighbors_num = sum([
            1 for (neighbor_i, neighbor_j) 
            in get_neigbor_indexes(i, j, len(grid), len(grid[0])) 
            if grid[neighbor_i][neighbor_j] == FILLED_CELL])
        result_num += filled_neighbors_num <= MAX_FILLED_CELLS_AS_NEIGHBORS

print(result_num)


# Part 2

grid = read_data(4, True)
result_num = 0
should_try_next_step = True
while should_try_next_step:
    should_try_next_step = False
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != FILLED_CELL:
                continue
            filled_neighbors_num = sum([
                1 for (neighbor_i, neighbor_j) 
                in get_neigbor_indexes(i, j, len(grid), len(grid[0])) 
                if grid[neighbor_i][neighbor_j] == FILLED_CELL])
            if filled_neighbors_num <= MAX_FILLED_CELLS_AS_NEIGHBORS:
                grid[i][j] = EMPTY_CELL
                result_num += 1
                should_try_next_step = True

print(result_num)
