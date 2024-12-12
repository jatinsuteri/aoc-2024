with open('day4.txt', 'r') as f:
    data = f.read()
    grid = [list(line) for line in data.split('\n')]

res = 0
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

for r in range(len(grid)):
    for c in range(len(grid[0])):
        for dir in dirs:
            row, col = r,c
            for char in 'XMAS':
                if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != char:
                    break
                row+=dir[0]
                col+=dir[1]
            else:
                res+=1
print(res)

##part 2

res = 0
for r in range(1, len(grid) - 1):
    for c in range(1, len(grid[0])- 1):
        if grid[r][c] == 'A':
            tl = grid[r-1][c-1] 
            tr = grid[r-1][c+1]
            bl = grid[r+1][c-1]
            br = grid[r+1][c+1]
            # if (tl == 'M' and br == 'S') or (tl == 'S' and br == 'M'):
            #     if (tr == 'M' and bl == 'S') or (tr == 'S' and bl == 'M'):
            #         res += 1
            if sorted([tl,br]) == ['M', 'S'] and sorted([tr,bl]) == ['M', 'S']:
                res += 1
print(res)