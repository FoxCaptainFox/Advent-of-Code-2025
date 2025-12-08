from utils import read_data
import math

# Part 1

data = read_data(6)
numbers_original_orientation = [[int(x) for x in line.split()] for line in data[:-1]]
expression_numbers = [list(row) for row in zip(*numbers_original_orientation)]
math_symbols = data[-1].split()

grand_sum = 0
for i in range(len(expression_numbers)):
    if math_symbols[i] == "+":
        grand_sum += sum(expression_numbers[i])
    elif math_symbols[i] == "*":
        grand_sum += math.prod(expression_numbers[i])
print(grand_sum)


# Part 2

data_original_orientation = read_data(6, as_separate_characters=True)
data = [list(row) for row in zip(*data_original_orientation)]
grand_sum = 0

first_column_in_block = True
block_math_symbol = None
block_result = None

for column in data:
    if "".join(column).strip() != "":
        if first_column_in_block:
            block_result = int("".join(column[:-1]).strip())
            block_math_symbol = column[-1]
            first_column_in_block = False
        else:
            number = int("".join(column).strip())
            if block_math_symbol == "+":
                block_result += number
            elif block_math_symbol == "*":
                block_result *= number
    else:
        grand_sum += block_result
        first_column_in_block = True

# Accounts for the last block
grand_sum += block_result

print(grand_sum)
