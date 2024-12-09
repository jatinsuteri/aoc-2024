with open("day2.txt", 'r') as f:
    lines = f.readlines()

reports = [list(map(int, line.strip().split())) for line in lines]

total = 0
for report in reports:
    inc = (report[1] - report[0]) > 0
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if (inc and diff < 0) or (not inc and diff > 0) or diff == 0 or abs(diff) > 3:  
            break
    else: total+=1

print(total)

## part 2

def is_safe(report):
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if diff == 0 or abs(diff) > 3:  
            return False
        if i > 0:
            prev_diff = report[i] - report[i - 1]
            if (prev_diff > 0 and diff < 0) or (prev_diff < 0 and diff > 0):
                return False
    return True

total = 0
for report in reports:
    if is_safe(report):  
        total += 1
    else:
        
        dampened_safe = False
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1:] 
            if is_safe(modified_report):
                dampened_safe = True
                break
        if dampened_safe:
            total += 1

print(total)