lis1 = []
lis2 = []

with open('day1.txt', 'r') as f:
    for line in f:
        num1, num2 = map(int, line.split())
        lis1.append(num1)
        lis2.append(num2)

lis1.sort()
lis2.sort()

i = 0
diff = 0
while i < len(lis1):
    diff += abs(lis1[i] - lis2[i])
    i += 1
print(diff)

##part 2

from collections import Counter
counter_lis2 = Counter(lis2)
similarity = 0

for i in lis1:
    if i in counter_lis2:
        if counter_lis2[i]:
            similarity += counter_lis2[i] * i
print(similarity)