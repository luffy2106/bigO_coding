def add_one(input):
    source = [char for char in input]
    i = len(source) - 1
    while True:
        if ord(source[i]) < ord("z"):
            source[i] = chr(ord(source[i]) + 1)
            break
        if source[i] == "z":
            source[i] = "a"
        i = i - 1
    source = "".join(source)
    return source


def compare(source, dest):
    source = [char for char in source]
    dest = [char for char in dest]
    for i in range(0, len(source)):
        if source[i] < dest[i]:
            return True
    return False


in1 = input()
in2 = input()


exist = 0
in1_add = in1
while compare(in1_add, in2):
    in1_add = add_one(in1)
    if compare(in1_add, in2):
        print(in1_add)
        exist = 1
        break
    else:
        in1 = in1_add


if exist == 0:
    print("No such string")
