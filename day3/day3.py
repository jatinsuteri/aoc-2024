with open('day3.txt', 'r') as f:
    corrupted_data = f.read()

import re
expression = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"

muls = re.findall(expression, corrupted_data)
res = 0
for a , b in muls:
    res += int(a) * int(b)
print(res)

##part 2

do_list = corrupted_data.split('do()')
do_list = [x.split("don't()")[0] for x in do_list]

res = 0
for do in do_list:
    matches = re.findall(expression, do)
    for x, y in matches:
        res += int(x) * int(y)

print(res)