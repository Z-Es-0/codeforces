for _ in range(int(input())):
    n=int(input())
    s=input()
    v=0
    for i in s:
        if i=='+':
            v+=1
        else:
            v-=1
    print(abs(v))