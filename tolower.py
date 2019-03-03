p, t = list(map(int, input().split()))
solved = 0  # number of solved problems
for problem in range(p):
    passed_case = 0
    for test in range(t):
        c = list(input())  # read string as last
        if ord(c[0]) < 97:  # if less than ascii value of 'a'
            c[0] = chr(ord(c[0]) + 32)  # Anthony's solution
        if str(c) == str(c).lower():
            passed_case += 1
    if passed_case == t:  # if all test cases passed
        solved += 1
print(solved)
