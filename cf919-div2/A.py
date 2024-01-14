t = int(input())
for _ in range(t):
    n = int(input())
    min_value, max_value = -float('inf'), float('inf')
    no = set()
    for _ in range(n):
        a, x = map(int, input().split())
        if a == 1:
            min_value = max(min_value, x)
        elif a == 2:
            max_value = min(max_value, x)
        else:
            no.add(x)
    if min_value > max_value:
        print(0)
        continue
 
 
    answer = max_value - min_value + 1
    for x in no:
        if min_value <= x <= max_value:
            answer -= 1
    print(answer)