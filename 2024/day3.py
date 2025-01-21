import re
import sys

input = open(sys.argv[1]).read()


pattern = r'mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don\'t\(\))'

matches = re.findall(pattern, input)

enabled = True
op = 0

for n1, n2, y, n in matches:
    if y == "do()":
        enabled = True
        continue
    elif n == "don't()":
        enabled = False
        continue
    else:
        if enabled:
            op += int(n1)*int(n2)

# Part 1
#print(sum([(int(num1)*int(num2)) for num1, num2 in matches]))

# Part 2
print(op)

