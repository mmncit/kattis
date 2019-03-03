m, a, b, c = list(map(int, input().split()))  # read inputs
if [a, b, c].count(m) >= 2:  # if 2 guys select all
    print("impossible")  # the last guy has to select at least 1
elif (a + b) > m and c > (2 * m - (a + b)):  # if choices of two guys overlaps with the last guy
    print("impossible")
else:
    print("possible")
