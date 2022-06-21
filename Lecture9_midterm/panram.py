import string

n = int(input())
str_n = [c for c in input()]

set_char = set(list(string.ascii_lowercase))
unique = 0
for c in str_n:
    if c.lower() in set_char:
        set_char.remove(c.lower())


if len(set_char) == 0:
    # print(unique)
    print("YES")
else:
    # print(unique)
    print("NO")
