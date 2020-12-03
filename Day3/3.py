def slopes(tree_map, right, down):
    index, row, tree_counter = 0, 0, 0
    text_length = len(tree_map[0])
    while row != len(tree_map) - 1:
        index += right
        row += down
        if index >= text_length:
            index = index - text_length
        position = tree_map[row][index]

        if position == "#":
            tree_counter += 1

    print(tree_counter)
    return tree_counter


def main():
    with open("3.txt", "r") as f:
        lines = f.readlines()
        tree_map = []
        for line in lines:
            tree_map.append(line.strip())
    final_answer = 0
    final_answer += slopes(tree_map, 1, 1)
    final_answer *= slopes(tree_map, 3, 1)
    final_answer *= slopes(tree_map, 5, 1)
    final_answer *= slopes(tree_map, 7, 1)
    final_answer *= slopes(tree_map, 1, 2)
    print(final_answer)


main()
