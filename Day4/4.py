def create_passports():
    passports = []
    with open("4.txt", "r") as f:
        passport = ""
        for line in f:
            if line.strip() == "":
                fields = passport.strip().split(" ")
                current_passport = {x.split(":")[0].strip(): x.split(":")[1].strip() for x in fields}
                passports.append(current_passport)
                passport = ""
            else:
                passport += " " + line.strip()
    return passports


def check_passport(passport):
    return len(passport) == 8 or (len(passport) == 7 and "cid" not in passport)


def check_passport_2(passport):
    byr = int(passport["byr"])
    byr_valid = len(str(byr)) == 4 and 1920 <= byr <= 2002
    iyr = int(passport["iyr"])
    iyr_valid = len(str(iyr)) == 4 and 2010 <= iyr <= 2020
    eyr = int(passport["eyr"])
    eyr_valid = len(str(eyr)) == 4 and 2020 <= eyr <= 2030
    hgt_w = passport["hgt"]
    hgt_valid = True if (hgt_w[-2::1] == "in" and 59 <= int(hgt_w[:-2]) <= 76) or (hgt_w[-2::1] == "cm" and 150 <= int(hgt_w[:-2]) <= 193) else False
    hcl = passport["hcl"]
    hcl_valid = True if hcl[0] == "#" and len(hcl) == 7 else False
    ecl_valid = passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    pid_valid = len(passport["pid"]) == 9

    return byr_valid and iyr_valid and eyr_valid and hgt_valid and hcl_valid and ecl_valid and pid_valid


def main():
    passports = create_passports()
    valid_passwords = [passport for passport in passports if check_passport(passport)]
    print(len(valid_passwords))
    more_valid_passwords = [passport for passport in valid_passwords if check_passport_2(passport)]
    print(len(more_valid_passwords))


main()
