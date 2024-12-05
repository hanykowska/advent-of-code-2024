
input_data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

input_data = input_data.split("\n\n")
print(len(input_data))

rules = input_data[0].split("\n")
updates = input_data[1].split("\n")

rules = [rule.split("|") for rule in rules]
rules = [[int(rule[0]), int(rule[1])] for rule in rules]

updates = [update.split(",") for update in updates]
updates = [[int(page) for page in update] for update in updates]
print(updates)
