from utils import read_data

# Part 1

raw_data = read_data(2)[0]

ranges = [
    [int(raw_range.split("-")[0]), int(raw_range.split("-")[1])] 
    for raw_range in raw_data.split(",")]

invalid_ids = []

for (range_start, range_end) in ranges:
    for id in range(range_start, range_end + 1):
        id_as_string = str(id)
        
        if len(id_as_string) % 2 != 0:
            continue
        
        half_len = int(len(id_as_string) / 2)
        if id_as_string[:half_len] == id_as_string[half_len:]:
            invalid_ids.append(id)

print(sum(invalid_ids))

# Part 2

raw_data = read_data(2)[0]

ranges = [
    [int(raw_range.split("-")[0]), int(raw_range.split("-")[1])] 
    for raw_range in raw_data.split(",")]

invalid_ids = []

# Checking each range
for (range_start, range_end) in ranges:
    # Checking each id
    for id in range(range_start, range_end + 1):
        id_as_string = str(id)
        id_len = len(id_as_string)
        # Checking each possible id split
        for split_parts_count in range(1, id_len + 1):
            if split_parts_count == 1 or id_len % split_parts_count != 0:
                continue
            split_parts_len = int(id_len / split_parts_count)
            first_potentially_repeating_part = id_as_string[:split_parts_len]
            if id_as_string == first_potentially_repeating_part * split_parts_count:
                invalid_ids.append(id)
                break

print(sum(invalid_ids))
