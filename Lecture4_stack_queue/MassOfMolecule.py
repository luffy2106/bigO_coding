
molecule = input()
stack = []
for c in molecule:
    if c == "(":
        stack.append(c)
    elif c == "C":
        stack.append(12)
    elif c == "H":
        stack.append(1)
    elif c == "O":
        stack.append(16)
    elif c.isdigit():
        stack[-1] = stack[-1] * int(c)
    elif c == ")":
        sum_medium = 0
        while True:
            top = stack.pop()
            if top == "(":
                break
            sum_medium = sum_medium + top
        stack.append(sum_medium)

print(sum(stack))