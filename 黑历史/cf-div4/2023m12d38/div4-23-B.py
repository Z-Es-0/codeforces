def fin(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == '?':
 
                missing = {'A', 'B', 'C'}
                missing -= set(grid[i])
                for k in range(3):
                    missing.discard(grid[k][j])
                return missing.pop()
 
t = int(input())
for _ in range(t):
    grid = [list(input().strip()) for _ in range(3)]
    print(fin(grid))