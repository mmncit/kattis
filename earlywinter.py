n, d_m = list(map(int, input().split()))
d_i = list(map(int, input().split()))
if any(i <= d_m for i in d_i):
    k = 0
    for val in d_i:
        if val > d_m:
            k += 1
        else:
            break
    print("It hadn't snowed this early in", k, "years!")
else:
    print("It had never snowed this early!")
