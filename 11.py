from collections import defaultdict
from utils import read_data

# Part 1

START_DEVICE = "you"
END_DEVICE = "out"

devices = {line.split(": ")[0]:line.split(": ")[1].split() for line in read_data(11)}

possible_paths = {tuple([START_DEVICE])}
possible_paths_num = 0

while possible_paths:
    new_possible_paths = set()
    for possible_path in possible_paths:
        if possible_path[-1] == END_DEVICE:
            possible_paths_num += 1
            continue
        for output in devices[possible_path[-1]]:
            new_possible_paths.add(possible_path + (output, ))
    possible_paths = new_possible_paths

print(possible_paths_num)


# Part 2

START_DEVICE = "svr"
STOP_1 = "fft"
STOP_2 = "dac"
END_DEVICE = "out"

devices_and_outputs = {line.split(": ")[0]:line.split(": ")[1].split() for line in read_data(11)}
devices_and_inputs = defaultdict(list)
for device in devices_and_outputs:
    for output in devices_and_outputs[device]:
        devices_and_inputs[output] += [device]

ways_to_get_to_device = {START_DEVICE: 1}
ways_to_get_to_device_through_stop_1 = {START_DEVICE: 0}
ways_to_get_to_device_through_stop_2 = {START_DEVICE: 0}
ways_to_get_to_device_through_both_stops = {START_DEVICE: 0}

# God forbid this graph has loops
should_try_again = True
while should_try_again:
    should_try_again = False
    for device in devices_and_inputs:
        if device in ways_to_get_to_device:
            # we already took care of this device
            continue
        inputs = devices_and_inputs[device]
        if set(inputs).issubset(set(ways_to_get_to_device)):
            # we can calculate ways to go here
            should_try_again = True
            ways_to_get_to_device[device] = sum([ways_to_get_to_device[input] for input in inputs])

            if device == STOP_1:
                ways_to_get_to_device_through_stop_1[device] \
                    = ways_to_get_to_device[device]
            else:
                ways_to_get_to_device_through_stop_1[device] \
                    = sum([ways_to_get_to_device_through_stop_1[input] for input in inputs])
            
            if device == STOP_2:
                ways_to_get_to_device_through_stop_2[device] \
                    = ways_to_get_to_device[device]
            else:
                ways_to_get_to_device_through_stop_2[device] \
                    = sum([ways_to_get_to_device_through_stop_2[input] for input in inputs])
            
            if device == STOP_1:
                ways_to_get_to_device_through_both_stops[device] \
                    = ways_to_get_to_device_through_stop_2[device]
            elif device == STOP_2:
                ways_to_get_to_device_through_both_stops[device] \
                    = ways_to_get_to_device_through_stop_1[device]
            else:
                ways_to_get_to_device_through_both_stops[device] \
                    = sum([ways_to_get_to_device_through_both_stops[input] for input in inputs])
            
print(ways_to_get_to_device_through_both_stops[END_DEVICE])
