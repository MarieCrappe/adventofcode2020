def parse_entry(entry):
    contents = entry.split(':')
    password = contents[1].strip()
    policy = contents[0].split(' ')
    first_number, second_number = policy[0].split('-')
    letter = policy[1]
    return letter, int(first_number), int(second_number), password


def verify_first(entry):
    letter, first_number, second_number, password = parse_entry(entry)
    occurrences = password.count(letter)
    is_valid = (first_number <= occurrences <= second_number)
    return is_valid


def verify_second(entry):
    letter, first_number, second_number, password = parse_entry(entry)
    count_letter = int(password[first_number-1] == letter)
    count_letter += int(password[second_number-1] == letter)
    is_valid = (count_letter == 1)
    return is_valid


if __name__ == '__main__':
    with open("input.txt") as passwords_file:
        passwords = passwords_file.readlines()
        good_passwords_first_check = 0
        good_passwords_second_check = 0
        for entry in passwords:
            good_passwords_first_check += int(verify_first(entry))
            good_passwords_second_check += int(verify_second(entry))
        print(good_passwords_first_check, good_passwords_second_check)
