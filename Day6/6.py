def collect_groups():
    groups = []
    group = []
    with open("6.txt", "r") as f:
        for line in f.readlines():
            if line.strip():
                group.append("".join(sorted(line.strip())))
            else:
                groups.append(group)
                group = []
    return groups


def check_list_element_contain(checkable_list, letter):
    for ele in checkable_list:
        if letter not in ele:
            return False
    return True


def anyone_yes(collected_groups):
    yes_answers = 0
    for group in collected_groups:
        yes_answers_set = set()
        for person in group:
            yes_answers_set.update(list(person))
        yes_answers += len(yes_answers_set)
    return yes_answers


def everyone_yes(collected_groups):
    yes_answers = 0
    for group in collected_groups:
        for question in max(group):
            if check_list_element_contain(group, question):
                yes_answers += 1
    return yes_answers


def main():
    collected_groups = collect_groups()

    print(anyone_yes(collected_groups))
    print(everyone_yes(collected_groups))


main()
