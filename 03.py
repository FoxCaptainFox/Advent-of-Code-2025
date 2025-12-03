from utils import read_data

# Part 1

batteries = read_data(3, True, int)
result_sum = 0

for battery in batteries:
    max_first_digit = max(battery[:-1])
    max_first_digit_index = battery.index(max_first_digit)
    max_second_digit = max(battery[max_first_digit_index + 1:])
    result_sum += max_first_digit * 10 + max_second_digit

print(result_sum)


# Part 2

DIGITS_NUM = 12
batteries = read_data(3, True, int)
result_sum = 0

for battery in batteries:
    for digit_index in range(DIGITS_NUM):
        digits_left = DIGITS_NUM - digit_index - 1

        selected_digit = max(battery[:-digits_left or None])
        selected_digit_index = battery.index(selected_digit)
        battery = battery[selected_digit_index + 1:]

        result_sum += selected_digit * 10 ** digits_left

print(result_sum)
