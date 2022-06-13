def checkFasten(a, b):
    listn = map(int, b.split())
    n = int(a)
    ans = "NO"
    num1 = 0
    num0 = 0
    for e in listn:
        if e == 0:
            num0 += 1
        if e == 1:
            num1 += 1
    num1 == 1
    if n == 1:
        if num1 == 1:
            return "YES"
    else:
        if num1 == n - 1:
            return "YES"
    return ans


n = 3
listn = [1]

print(checkFasten(n, listn))
