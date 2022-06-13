N = int(input())
interest_m = [int(x) for x in input().split()]
stack = [interest_m[0]]
stop = 0

if len(interest_m) == 1:
    if interest_m[0] > 15:
        stop = 15
    else:
        stop = interest_m[0] + 15
else:
    if interest_m[0] > 15:
        stop = 15
    else:
        for i in range(1, len(interest_m)):
            # if the last element:
            if i == len(interest_m) - 1:
                if interest_m[i] == 90:
                    stop = 90
                    break
                else:
                    if interest_m[i] - stack[-1] > 15:
                        stop = stack[-1] + 15
                        break
                    else:
                        stack.append(interest_m[i])
                        stop = stack[-1] + min(15, 90 - stack[-1])
                        break
            # If not last element
            else:
                if interest_m[i] - stack[-1] > 15:
                    stop = stack[-1] + 15
                    break
                else:
                    stack.append(interest_m[i])


print(stop)
