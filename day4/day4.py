filename = "day4_data.txt"

all_data = []
with open(filename, "r") as file:
    for line in file:
        all_data.append([char.strip() for char in line])
# print(all_data)

# Part 1


def find_num_xmas(data, row, col):
    num_xmas = 0

    # Look up
    up_word = ""
    for i in range(row - 1, row - 4, -1):
        if i < 0:  # Out of bounds
            break
        up_word += data[i][col]
    if up_word == "MAS":
        num_xmas += 1

    # Look northwest
    nw_word = ""
    for i in range(1, 4):
        if row - i < 0 or col - i < 0:
            break
        nw_word += data[row - i][col - i]
    if nw_word == "MAS":
        num_xmas += 1

    # Look west
    w_word = ""
    for i in range(1, 4):
        if col - i < 0:
            break
        w_word += data[row][col - i]
    if w_word == "MAS":
        num_xmas += 1

    # Look southwest
    sw_word = ""
    for i in range(1, 4):
        if row + i >= len(data) or col - i < 0:
            break
        sw_word += data[row + i][col - i]
    if sw_word == "MAS":
        num_xmas += 1

    # Look south
    s_word = ""
    for i in range(1, 4):
        if row + i >= len(data):
            break
        s_word += data[row + i][col]
    if s_word == "MAS":
        num_xmas += 1

    # Look southeast
    se_word = ""
    for i in range(1, 4):
        if row + i >= len(data) or col + i >= len(data[row]):
            break
        se_word += data[row + i][col + i]
    if se_word == "MAS":
        num_xmas += 1

    # Look east
    e_word = ""
    for i in range(1, 4):
        if col + i >= len(data[row]):
            break
        e_word += data[row][col + i]
    if e_word == "MAS":
        num_xmas += 1

    # Look northeast
    ne_word = ""
    for i in range(1, 4):
        if row - i < 0 or col + i >= len(data[row]):
            break
        ne_word += data[row - i][col + i]
    if ne_word == "MAS":
        num_xmas += 1

    return num_xmas


num_xmas = 0
for row in range(len(all_data)):
    for col in range(len(all_data[row])):
        if all_data[row][col] == "X":
            num_xmas += find_num_xmas(all_data, row, col)
            # print(find_num_xmas(all_data, row, col))
print(num_xmas)

# Part 2


def find_mas(data, row, col):
    top_left = data[row - 1][col - 1] if (row - 1 >= 0 and col - 1 >= 0) else ""
    top_right = (
        data[row - 1][col + 1] if row - 1 >= 0 and col + 1 < len(data[row]) else ""
    )
    bottom_left = data[row + 1][col - 1] if row + 1 < len(data) and col - 1 >= 0 else ""
    bottom_right = (
        data[row + 1][col + 1]
        if row + 1 < len(data) and col + 1 < len(data[row])
        else ""
    )

    # Return for non-M/S characters
    for test in [top_left, top_right, bottom_left, bottom_right]:
        if test not in ["M", "S"]:
            return 0
    
    # Check for MAS crosses
    check = [top_left, bottom_right, top_right, bottom_left]
    if check not in [
        ["M", "S", "M", "S"],
        ["M", "S", "S", "M"],
        ["S", "M", "M", "S"],
        ["S", "M", "S", "M"],
    ]:
        return 0
    else:
        return 1

num_crosses = 0
for row in range(len(all_data)):
    for col in range(len(all_data[row])):
        if all_data[row][col] == "A":
            num_crosses += find_mas(all_data, row, col)
print(num_crosses)
