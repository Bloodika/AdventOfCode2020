def find_bad_number(lines):
    index = 24
    while index < len(lines) - 1:
        search_number = int(lines[index + 1])
        found = False
        for i in range(index - 24, index + 1):
            for j in range(i + 1, index + 1):
                if int(lines[i]) + int(lines[j]) == search_number:
                    found = True
                    break
        if not found:
            return search_number
        index += 1


def find_range(bad_number, lines):
    found = False
    index = 0
    while not found:
        numbers = []
        for i in range(index, len(lines)):
            numbers.append(int(lines[i]))
            if sum(numbers) == bad_number:
                return numbers
            elif sum(numbers) > bad_number:
                index += 1
                break


with open("9.txt", "r") as f:
    lines = f.readlines()
    bad_number = find_bad_number(lines)
    print(bad_number)
    found_range = find_range(bad_number, lines)
    print(min(found_range)+max(found_range))
