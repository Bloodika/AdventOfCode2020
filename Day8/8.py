import copy


def search_for_loop(lines):
    steps = []
    index = 0
    acc = 0
    while index not in steps:
        steps.append(index)
        try:
            if "acc" in lines[index]:
                acc += int(lines[index].split("acc")[1])
                index += 1
            elif "nop" in lines[index]:
                index += 1
            elif "jmp" in lines[index]:
                index += int(lines[index].split("jmp")[1])
        except:
            print("haha",acc)

    return acc


def search_in_list(s, li):
    indexes = []
    for l in range(0, len(li)):
        if s in li[l]:
            indexes.append(l)
    return indexes


def fix_loop(lines):
    nops = search_in_list("nop", lines)
    jmps = search_in_list("jmp", lines)
    for i in nops:
        copy_lines = copy.deepcopy(lines)
        copy_lines[i] = copy_lines[i].replace("nop", "jmp")
        search_for_loop(copy_lines)
    for j in jmps:
        copy_lines = copy.deepcopy(lines)
        copy_lines[j] = copy_lines[j].replace("jmp", "nop")
        search_for_loop(copy_lines)


def main():
    with open("8.txt", "r") as f:
        lines = f.readlines()
        print(search_for_loop(lines))
        fix_loop(lines)


main()
