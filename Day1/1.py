with open("1.txt", "r") as f:
    af = f.readlines()
    [print(int(x) * int(y)) for x in af for y in af if int(x) + int(y) == 2020]
    [print(int(x) * int(y) * int(z)) for x in af for y in af for z in af if int(x) + int(y) + int(z) == 2020]
