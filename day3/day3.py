import re


file = 'day3_data.txt'

string = None
with open(file, 'r') as f:
    string = f.read()
# print(string)

## Part 1
expression = r'mul\([0-9]{0,4},[0-9]{0,4}\)'

matches = re.findall(expression, string)

# print(matches)

value = 0
for match in matches:
    match = match.replace('mul(', '')
    match = match.replace(')', '')
    match = match.split(',')
    value += int(match[0]) * int(match[1])
print(value)

## Part 2
expression = r"mul\([0-9]{0,4},[0-9]{0,4}\)|don't\(\)|do\(\)"

matches = re.findall(expression, string)
print(matches)

value = 0
enable = True
for match in matches:
    if'don' in match:
        enable = False
        continue
    elif 'do' in match:
        enable = True
        continue

    if not enable:
        continue

    match = match.replace('mul(', '')
    match = match.replace(')', '')
    match = match.split(',')
    value += int(match[0]) * int(match[1])
print(value)
