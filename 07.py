from collections import defaultdict
from utils import read_data

START_CHAR = "S"
EMPTY_CHAR = "."
SPLITTER_CHAR = "^"


# Paer 1

data = read_data(7, as_separate_characters=True)
start_position = data[0].index(START_CHAR)
current_beam_positions = {start_position}
split_number = 0

for row in data:
    new_beam_positions = set()
    for beam_position in current_beam_positions:
        if row[beam_position] == SPLITTER_CHAR:
            new_beam_positions.add(beam_position - 1)
            new_beam_positions.add(beam_position + 1)
            split_number += 1
        else:
            new_beam_positions.add(beam_position)
    current_beam_positions = new_beam_positions

print(split_number)


# Part 2

data = read_data(7, as_separate_characters=True)
start_position = data[0].index(START_CHAR)
current_beam_positions_and_ways_to_get_there = defaultdict(int, {start_position: 1})

for row in data:
    new_beam_positions_and_ways_to_get_there = defaultdict(int)
    for beam_position, ways_to_get_there in current_beam_positions_and_ways_to_get_there.items():
        if row[beam_position] == SPLITTER_CHAR:
            new_beam_positions_and_ways_to_get_there[beam_position - 1] += ways_to_get_there
            new_beam_positions_and_ways_to_get_there[beam_position + 1] += ways_to_get_there
        else:
            new_beam_positions_and_ways_to_get_there[beam_position] += ways_to_get_there
    current_beam_positions_and_ways_to_get_there = new_beam_positions_and_ways_to_get_there

print(sum(current_beam_positions_and_ways_to_get_there.values()))
