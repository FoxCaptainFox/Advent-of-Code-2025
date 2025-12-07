from utils import read_data

data_as_strings = read_data(5)
data_separator_index = data_as_strings.index("")
ranges_as_str = data_as_strings[:data_separator_index]
values_as_str = data_as_strings[data_separator_index + 1:]
ranges = [[int(x) for x in range_string.split("-")] for range_string in ranges_as_str]
ids = [int(x) for x in values_as_str]


# Part 1

is_id_fresh = [False] * len(ids)
for (range_start, range_end) in ranges:
    for i in range(len(ids)):
        if range_start <= ids[i] <= range_end:
            is_id_fresh[i] = True

print(sum(is_id_fresh))


# Part 2

ranges_sorted_by_start = sorted(ranges[:], key=lambda x: x[0])
ranges_without_overlap = []
for (range_start, range_end) in ranges_sorted_by_start:
    max_included_id = max((x[1] for x in ranges_without_overlap), default=None)
    if max_included_id is not None and range_start <= max_included_id:
        continue
    current_range_end = range_end
    while True:
        new_range_end = max([end for (start, end) in ranges if start <= current_range_end])
        if current_range_end == new_range_end:
            break
        current_range_end = new_range_end
    ranges_without_overlap.append((range_start, current_range_end))
print(sum([end - start + 1 for (start, end) in ranges_without_overlap]))
