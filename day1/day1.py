data_file = 'day1_data.txt'

left = []
right = []
with open(data_file) as f:
    for row in f:
        left_val, right_val = [int(num.strip()) for num in row.split(' ') if num.strip() != '']
        left.append(left_val)
        right.append(right_val)
        # print(data)
# print(left, right)

left.sort()
right.sort()

## Part 1

# value = 0
# while left != [] and right != []:
#     left_num = left.pop(0)
#     right_num = right.pop(0)
#
#     value += abs(left_num - right_num)
# print(value)

## Part 2

value = 0
while left != []:
    left_num = left.pop(0)
    count = right.count(left_num)
    if count == 0:
        continue

    value += (count * left_num)
print(value)
