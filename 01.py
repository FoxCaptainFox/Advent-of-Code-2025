from utils import read_data

# Part 1

dial_at = 50
times_dial_at_0 = 0

data_as_str_lines = read_data(1)
for line in data_as_str_lines:
    direction = -1 if line[0] == "L" else 1
    distance = int(line[1:])
    dial_at = (dial_at + direction * distance) % 100
    if dial_at == 0:
        times_dial_at_0 += 1

print(times_dial_at_0)


# Part 2

dial_at = 50
times_dial_at_0 = 0

data_as_str_lines = read_data(1)
for line in data_as_str_lines:
    direction = -1 if line[0] == "L" else 1
    distance = int(line[1:])
    for _ in range(distance):
        dial_at = (dial_at + direction) % 100
        if dial_at == 0:
            times_dial_at_0 += 1

print(times_dial_at_0)
