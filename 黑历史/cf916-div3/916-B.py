def ge(a, b):
    result = []
    if a==2 :
        if b==1:
            result=[1,2]
        else:
            result=[2,1]
        return result
    else:
        for i in range(1, b + 1):
            result.append(i)
        for i in range(a, b, -1):
            result.append(i)
        return result
for _ in range(int(input())):
    a, b = map(int, input().split())
    output = ge(a, b)
    print(' '.join(map(str,output)))