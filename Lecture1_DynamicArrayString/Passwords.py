nk = [int(e) for e in input().split(" ")]
n = nk[0]
k = nk[1]

list_pass = []
for i in range(0, n):
    list_pass.append(input())

correct = input()


def count(list_pass, correct):
    len_correct = len(correct)
    count_less = 0
    count_equal = 0
    count_correct = 0
    for e in list_pass:
        if e == correct:
            count_correct += 1
        if len(e) < len_correct:
            # print(e)
            count_less += 1
        if len(e) == len_correct:
            count_equal += 1
    return count_less, count_equal, count_correct


count_less, count_equal, count_correct = count(list_pass, correct)
wrong_ans_less = count_less
wrong_ans_equal = count_equal - count_correct
wrong_ans = wrong_ans_less + wrong_ans_equal


if count_correct > 0:
    best_time = count_less // k * (k + 5) + count_less % k + 1
    worst_time = wrong_ans // k * (k + 5) + wrong_ans % k + 1
else:
    worst_time = n // k * (k + 5) + n % k
    best_time = worst_time

print(str(best_time) + " " + str(worst_time))
