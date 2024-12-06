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