def search_for_colors(lines):
    can_contain = set([line.split("contain")[0].split("bag")[0].strip() for line in lines if
                       "shiny gold" in line.split("contain")[1].strip()])
    before_size = len(can_contain)
    now_size = 0
    while before_size != now_size:
        before_size = len(can_contain)
        can_contain.update([line.split("contain")[0].split("bag")[0].strip() for line in lines if
                            any(bag in line for bag in can_contain)])
        now_size = len(can_contain)
    return can_contain


def split_it(line):
    splitted = {" ".join(sp.strip().split(" ")[1:-1]): sp.strip().split(" ")[0] for sp in
                line.split("contain")[1].strip().split(",")}
    summ = 0
    for sp in splitted.values():
        if sp != "no":
            summ += int(sp)
        else:
            summ = 1
    splitted["summ"] = summ
    return splitted


def search_in_list_by_keys(search, search_map):
    return next(item[search] for item in search_map if search in item.keys())


def rec_search(item, bags_in_map, final_result, s):
    for key in item.keys():
        if key not in ["other", "summ"]:
            found = search_in_list_by_keys(key, bags_in_map)
            print(key, s)
            if key not in final_result:
                final_result[key] = [int(item[key]) * s]
            else:
                final_result[key].append(int(item[key])*s)
            s = int(item[key]) * s
            rec_search(found, bags_in_map, final_result, s)


def shiny_bag_bags(lines):
    bags_in_map = [{line.split("contain")[0].split("bag")[0].strip(): split_it(line)} for line in lines]
    item = search_in_list_by_keys("shiny gold", bags_in_map)
    final_result = {}
    print(bags_in_map)
    rec_search(item, bags_in_map, final_result, 1)
    summ = 0
    print(final_result)
    for a, b in final_result.items():
        summ += sum(b)
    print(summ)


def main():
    with open("7.txt", "r") as f:
        lines = f.readlines()
        can_contain = search_for_colors(lines)
        print(len(can_contain))
        shiny_bag_bags(lines)


main()
