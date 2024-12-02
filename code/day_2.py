import os

input_name = "input_2.txt"
input_path = "../inputs/" + input_name
# in macOS or pycharm, ".." is needed to get out of "code" directory,
# in Windows or VSCode, the starting point is the repository directory

file = open(os.path.abspath(input_path), "r")
input_data = file.read()
# input_data = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9"""
input_data = input_data.split("\n")

safe_reports = 0

def check_if_safe(numbers):
    return (
        all((j - i) <= 3 and (j-i) > 0 for i, j in zip(numbers, numbers[1:]))
        or
        all((i - j) <= 3 and (i - j) > 0 for i, j in zip(numbers, numbers[1:]))
    )


for k, report in enumerate(input_data):
    if report == '':
        continue
    report = report.split(" ")
    report = [int(x) for x in report]
    for i in range(len(report)):
        report_cp = report[:]
        del report_cp[i]
        if check_if_safe(report_cp):
            safe_reports += 1
            break


print(safe_reports)


file.close()


# solution adjusted based on https://www.geeksforgeeks.org/python-check-if-list-is-strictly-increasing/
