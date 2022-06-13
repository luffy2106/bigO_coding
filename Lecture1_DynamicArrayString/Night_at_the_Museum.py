text = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
alpha_list = [a for a in alpha]
score = 0
pointer = "a"


def navigate(distance, x):
    if distance > x / 2:
        return -1
    else:
        return 1


for char in text:
    distance = alpha_list.index(char) - alpha_list.index(pointer)
    move = min(distance, len(alpha_list) - distance)
    navigator = navigate(distance, len(alpha_list))
    real_move = move * navigator
    print(move)
    score = score + abs(move)
    pointer = char
    alpha_list = alpha_list[real_move:] + alpha_list[:real_move]


print(score)
