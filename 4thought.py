from itertools import product

# Check all permutations with repetitions
table = {}
for a, b, c in product([' + ', ' - ', ' * ', ' // '], repeat=3):
    exp = "4{:s}4{:s}4{:s}4".format(a, b, c)
    val = eval(exp)
    table[val] = exp.replace('//', '/') + " = {:d}".format(val)

for i in range(0, int(input())):
    n = int(input())
    if n < -60 or n > 256 or n not in table:
        print("no solution")
    else:
        print(table[n])
