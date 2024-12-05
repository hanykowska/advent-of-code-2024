import os


input_name = "input_5.txt"
input_path = "inputs/" + input_name
# in macOS or pycharm, ".." is needed to get out of "code" directory,
# in Windows or VSCode, the starting point is the repository directory

file = open(os.path.abspath(input_path), "r")
input_data = file.read()
file.close()

# input_data = """47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47"""

input_data = input_data.split("\n\n")
print(len(input_data))

rules = input_data[0].splitlines()
updates = input_data[1].splitlines()

rules = sorted(rules)
rules = [rule.split("|") for rule in rules]
rules = [[int(rule[0]), int(rule[1])] for rule in rules]

updates = [update.split(",") for update in updates]
updates = [[int(page) for page in update] for update in updates]

rules_dict = {}
for rule in rules:
    if rule[0] in rules_dict:
        rules_dict[rule[0]].append(rule[1])
    else:
        rules_dict[rule[0]] = [rule[1]]


valid_updates = []
for i,update in enumerate(updates):
    update_ok = 1
    for m, val_m in enumerate(update):
        if m == len(update)-1:
            break
        try:
            if all(val_n in rules_dict[val_m] for val_n in update[m+1:]):
                pass
                #no change needed, the update is ok
            else:
                update_ok = 0
                break
        except KeyError:
            update_ok = 0
            break
        
    if update_ok:
        valid_updates.append([i,update[len(update)//2]])

print(valid_updates)

print(sum(x[1] for x in valid_updates))

