def main():
    t = int(input())
    for _ in range(t):
        xs = set()
        ys = set()

        for _ in range(4):
            x, y = map(int, input().split())
            xs.add(x)
            ys.add(y)

        length = abs(max(xs) - min(xs))
        if len(xs) == 1:
            length = abs(max(ys) - min(ys))

        area = length ** 2
        print(area)


if __name__ == "__main__":
    main()