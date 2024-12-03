import re
import os


input_name = "input_3.txt"
input_path = "../inputs/" + input_name
# in macOS or pycharm, ".." is needed to get out of "code" directory,
# in Windows or VSCode, the starting point is the repository directory

file = open(os.path.abspath(input_path), "r")
input_data = file.read()
file.close()
# input_data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
# input_data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

input_data = re.findall(r'(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don\'t\(\))', input_data, flags=0)
print("multiplications found: ",len(input_data))

multiplications = []
enabled = 1
for i,mul in enumerate(input_data):
    if re.match("(do\(\))",mul[1]):
        enabled = 1
    elif re.match("(don\'t\(\))",mul[2]):
        enabled = 0
    elif enabled:
        nums = re.findall(r'(\d+)', mul[0],  flags=0)
        if len(nums) != 2:
            print("extracted numbers are incorrect: ", nums)
            continue
        multiplications.append(int(nums[0]) * int(nums[1]))


print(sum(multiplications))


