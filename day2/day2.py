data_file = 'day2_data.txt'

data = []
with open(data_file) as f:
    for row in f:
        data.append([int(num.strip()) for num in row.split(' ') if num.strip() != ''])
# print(data)

def check_row(row: list):
    temp_front = None
    temp_back = None
    gradual = None
    for val in row:
        if temp_back is None:
            temp_back = val
            continue

        temp_front = val

        # First handle the difference between the two values
        diff = abs(temp_front - temp_back)
        if diff < 1 or diff > 3:
            temp_back = temp_front
            return False

        # Then handle the gradual difference
        temp_gradual = temp_front - temp_back
        if temp_gradual > 0:
            temp_gradual = 1
        elif temp_gradual < 0:
            temp_gradual = -1
        
        if gradual is None:
            gradual = temp_gradual
        elif gradual != temp_gradual:
            temp_back = temp_front
            return False

        temp_back = temp_front
    return True


## Part 1
safe = 0
for row in data:
    if check_row(row):
        safe += 1

print(safe)

## Part 2
safe = 0
for row in data:
    if check_row(row):
        safe += 1
        continue

    for i in range(len(row)):
        temp_row = row.copy()
        temp_row.pop(i)
        if check_row(temp_row):
            safe += 1
            break
    
print(safe)

