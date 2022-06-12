n = int(input())
list_input = []
for i in range(0,n):
    exp = input().split()
    list_input.append(exp)

for i in range(0,n):
    exp = input().split()
    stack_operator = []
    RPN = ""
    for char in exp:
        if char.isalpha():
            RPN = RPN + char
        if char in ['+', '-', '*', '/', '^']:
            stack_operator.append(char)
        if char == ")":
            RPN = RPN + stack_operator[-1]
            stack_operator.pop()
    
