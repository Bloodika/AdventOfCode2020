class Policy:
    def __init__(self, text):
        validation = text.split(":")[0].strip()
        number_validation = validation.split(" ")[0]

        self.password = text.split(":")[1].strip()
        self.letter = validation.split(" ")[1]
        self.min_number = int(number_validation.split("-")[0])
        self.max_number = int(number_validation.split("-")[1])

    def check_first_condition(self, counter):
        return self.max_number >= counter >= self.min_number

    def check_second_condition(self):
        a = self.password[self.min_number - 1] == self.letter and self.password[self.max_number - 1] != self.letter
        b = self.password[self.min_number - 1] != self.letter and self.password[self.max_number - 1] == self.letter
        return a or b


def main():
    with open("2.txt", "r") as f:
        af = f.readlines()
        first_valid_counter = 0
        second_valid_counter = 0
        for current_line in af:
            current_policy = Policy(current_line)

            counter = 0
            for pw in current_policy.password:
                if pw == current_policy.letter:
                    counter += 1

            if current_policy.check_first_condition(counter):
                first_valid_counter += 1

            if current_policy.check_second_condition():
                second_valid_counter += 1

        print(first_valid_counter)
        print(second_valid_counter)


main()
