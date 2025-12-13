import math
from utils import read_data
import numpy as np
from itertools import product


# Part 1

minimal_steps_sum = 0

for row in read_data(10):
    desired_lights_raw, *switches_raw, joltages_raw = row.split()
    desired_lights = tuple(char == "#" for char in desired_lights_raw[1:-1])
    switches = [[int(x) for x in switch[1:-1].split(",")] for switch in switches_raw]

    lights_num = len(desired_lights)
    initial_lights = tuple([False] * lights_num)
    possible_light_configurations = set([initial_lights])
    steps = 0
    while desired_lights not in possible_light_configurations:
        new_possible_light_configurations = set()
        for possible_light_configuration in possible_light_configurations:
            for switch in switches:
                new_possible_light_configurations.add(tuple(
                    possible_light_configuration[index] ^ (index in switch)
                    for index in range(lights_num)
                ))
        possible_light_configurations = new_possible_light_configurations
        steps += 1
    minimal_steps_sum += steps

print(minimal_steps_sum)


# Part 2

# minimal_steps_sum = 0
# line = 0

# for row in read_data(10):
#     print(f"{line:3}/151")
#     line += 1
#     desired_lights_raw, *switches_raw, joltages_raw = row.split()
#     switches = [[int(x) for x in switch[1:-1].split(",")] for switch in switches_raw]
#     desired_joltages = tuple(int(x) for x in joltages_raw[1:-1].split(","))
# 
#     joltages_num = len(desired_joltages)
#     initial_joltages = tuple([0] * joltages_num)
#     possible_joltage_configurations = set([initial_joltages])
#     steps = 0
#     while desired_joltages not in possible_joltage_configurations:
#         new_possible_joltage_configurations = set()
#         for possible_joltage_configuration in possible_joltage_configurations:
#             for switch in switches:
#                 new_possible_joltage_configurations.add(tuple(
#                     possible_joltage_configuration[index] + int(index in switch)
#                     for index in range(joltages_num)
#                 ))
#         possible_joltage_configurations = new_possible_joltage_configurations
#         steps += 1
#     minimal_steps_sum += steps
# 
# print(minimal_steps_sum)

minimal_steps_sum = 0



for row in read_data(10):
    desired_lights_raw, *switches_raw, joltages_raw = row.split()
    switches = [[int(x) for x in switch[1:-1].split(",")] for switch in switches_raw]
    desired_joltages = tuple(int(x) for x in joltages_raw[1:-1].split(","))
    joltages_num = len(desired_joltages)
    
    # which joltages each button controls: [[3], [1, 3], [2], [2, 3], [0, 2], [0, 1]] ->
    # which buttons control each joltage [[4, 5], [1, 5], [2, 3, 4], [0, 1, 3]]
    joltage_switches = \
         [[switch for switch in range(len(switches)) if joltage in switches[switch]] \
            for joltage in range(joltages_num)]
    joltage_switches_sorted = sorted(joltage_switches, key = lambda x: len(x))
    
    
    # variable reduction ✨
    # we don't actually need all the variables
    # some could be calculated from others
    # e.g., if first joltage is controlled by 4th and 5th button, we can get one value from another
    # true - primary varaible, false - calculated varaible, None - TBD
    is_switch_important = [None] * len(switches)
    for joltage_switch in joltage_switches_sorted:
        undecided_variables = [js for js in joltage_switch if is_switch_important[js] is None]
        if len(undecided_variables) == 0:
            # everything here is already covered
            continue
        elif len(undecided_variables) == 1:
            # we can caclculate it
            is_switch_important[undecided_variables[0]] = False
        else:
            for undecided_variable in undecided_variables[:-1]:
                is_switch_important[undecided_variable] = True
            is_switch_important[undecided_variables[-1]] = False
        
    # bruteforce ✨
    max_joltage = max(desired_joltages)
    important_switches_unsorted = [i for i in range(len(is_switch_important)) if is_switch_important[i]]
    # we should take switches with the most joltages controlled first
    important_switches = sorted(important_switches_unsorted, key=lambda switch: len(switches[switch]), reverse=True)

    def arrays(length, maxvalue):
        yield from product(range(maxvalue + 1), repeat=length)
    
    # minimal_steps = math.inf
    # for values_for_important_variables in arrays(len(important_switches), max_joltage):
    #     pass

    print(len(important_switches) ** max_joltage)


    
# 
#     # another approach:
#     joltages = tuple([0] * joltages_num)
#     while joltages != desired_joltages:
#         # 1) try pressing available buttonn with biggest number of controlled joltages
#         # 2) if there is at least one joltage above desired, don't press it, mark button as unavaliable
#         # 3) if there is available button, go to 1)
#         # 4) if there is no such button 

# def foo(switches_pressed):
#     # calculate is it okay now
#     if (switches_pressed for x in range(len(switches_sorted))) = desired_joltages:
#         return sum(switches_pressed)
#     # too much - return None
#     # exactly - return sum
#     # too few - check next
#     for switch in switches_sorted:
#         pass
# 
# 
# for row in read_data(10):
#     desired_lights_raw, *switches_raw, joltages_raw = row.split()
#     switches = [[int(x) for x in switch[1:-1].split(",")] for switch in switches_raw]
#     switches_sorted = sorted(switches, key = lambda switch: len(switch), reverse=True)
# 
#     desired_joltages = tuple(int(x) for x in joltages_raw[1:-1].split(","))
#     joltages_num = len(desired_joltages)
