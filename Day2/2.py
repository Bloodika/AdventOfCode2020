with open("2.txt", "r") as f:
    af = f.readlines()
    first_valid_counter = 0
    second_valid_counter = 0
    for line in af:
        validation = line.split(":")[0].strip()
        number_validation = validation.split(" ")[0]
        word_validation = validation.split(" ")[1]
        password = line.split(":")[1].strip()
        min_number = int(number_validation.split("-")[0]) - 1
        max_number = int(number_validation.split("-")[1]) - 1

        first_counter = 0
        for pw in password:
            if pw == word_validation:
                first_counter += 1

        if max_number >= first_counter >= min_number:
            first_valid_counter += 1
        if (password[min_number] == word_validation and password[max_number] != word_validation) or (password[min_number] != word_validation and password[max_number] == word_validation):
            second_valid_counter += 1
    print(first_valid_counter)
    print(second_valid_counter)
