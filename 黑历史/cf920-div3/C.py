def can_send_all_messages(n, f, a, b, moments):
    current_charge = f
    last_moment = 0

    for moment in moments:
        stay_on_cost = a * (moment - last_moment)
        if stay_on_cost < b:
            current_charge -= stay_on_cost
        else:
            current_charge -= b
        if current_charge <= 0:
            return "NO"
        last_moment = moment
    return "YES"
t = int(input())
for _ in range(t):
    n, f, a, b = map(int, input().split())
    moments = list(map(int, input().split()))
    print(can_send_all_messages(n, f, a, b, moments))