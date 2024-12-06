rules_file = 'day5_data_rules.txt'
pages_file = 'day5_data_pages.txt'

rules_data = []
with open(rules_file) as file:
    for line in file:
        rules_data.append(line.strip().split('|'))

pages_data = []
with open(pages_file) as file:
    for line in file:
        pages_data.append(line.strip().split(','))

def check_rules(rules: list, page_list: list):
    for rule in rules:
        first_rule, second_rule = rule

        # Check if both rules are in the page list
        if first_rule not in page_list or second_rule not in page_list:
            continue

        first_index = page_list.index(first_rule)
        second_index = page_list.index(second_rule)

        if first_index < second_index:
            continue
        else:
            return False
    return True

def find_middle_value(page_list: list):
    index = ((len(page_list) - 1) / 2)
    return page_list[int(index)]

# Part 1
value = 0
for page_list in pages_data:
    if check_rules(rules_data, page_list):
        middle_value = find_middle_value(page_list)
        value += int(middle_value)
print(value)

# Part 2
def get_new_list(rules: list, page_list: list):
    for rule in rules:
        first_rule, second_rule = rule
    
        # Check if both rules are in the page list
        if first_rule not in page_list or second_rule not in page_list:
            continue

        first_index = page_list.index(first_rule)
        second_index = page_list.index(second_rule)

        if first_index < second_index:
            continue

        first_val = page_list.pop(first_index)
        page_list.insert(second_index, first_val)
        continue
    return page_list

value = 0
for page_list in pages_data:
    if not check_rules(rules_data, page_list):

        check = False
        while not check:
            page_list = get_new_list(rules_data, page_list)
            check = check_rules(rules_data, page_list)

        middle_value = find_middle_value(page_list)
        value += int(middle_value)
print(value)
