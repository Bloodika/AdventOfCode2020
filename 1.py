with open("1.txt", "r") as f:
    af = f.readlines()
    [[print(int(y) * int(x)) for y in af if int(x) + int(y) == 2020] for x in af]
    [[[print(int(y) * int(x) * int(z)) for z in af if int(x) + int(y) + int(z) == 2020] for y in af] for x in af]
