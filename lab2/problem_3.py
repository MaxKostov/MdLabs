def get_digit_substrings(input_string):
    current_substring = ""
    digit_substrings = []

    for char in input_string:
        if char.isdigit():
            current_substring += char
        elif current_substring:
            digit_substrings.append(current_substring)
            current_substring = ""

    # Add the last substring if it ends with digits
    if current_substring:
        digit_substrings.append(current_substring)

    return digit_substrings


def has_consecutive_numbers(input_string):
    has = []
    for i in range(len(input_string) - 1):
        current_char = input_string[i]
        next_char = input_string[i + 1]

        if current_char.isdigit() and next_char.isdigit():
            if int(next_char) == int(current_char) + 1:
                return True

    return False

def find_longest_consecutive_substring(input_string):
    current_substring = ""
    longest_substring = ""

    for i in range(len(input_string) - 1):
        current_char = input_string[i]
        next_char = input_string[i + 1]

        if current_char.isdigit() and next_char.isdigit() and int(next_char) == int(current_char) + 1:
            current_substring += current_char
        else:
            current_substring += current_char
            if len(current_substring) > len(longest_substring):
                longest_substring = current_substring
            current_substring = ""

    # Include the last character in the substring if it is part of the consecutive sequence
    if current_substring and input_string[-1].isdigit() and int(input_string[-1]) == int(current_substring[-1]) + 1:
        current_substring += input_string[-1]

    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring

    return longest_substring
def main():
    crit = {'lower' : 0,
    'upper' : 0,
    'num' : 0,
    'spec' : 0}

    triplets = 0
    steps = 0

    password = input("password = ")

    if ' ' in password:
        exit("You are not allowed to use space in the password")

    if len(password) < 8:
        steps += 8-len(password)

    if len(password) > 20:
        steps += len(password) - 20

    for i in password:
        if i.islower():
            crit['lower'] += 1
        if i.isupper():
            crit['upper'] += 1
        if i.isdigit():
            crit['num'] += 1
        if not i.isalnum() and not i.isspace():
            crit['spec'] += 1

    count_of_zeros = sum(value == 0 for value in crit.values())

    if count_of_zeros != 0:
        steps += count_of_zeros

    passtrip = password[:].lower()
    for i in range(len(passtrip) - 2):
        cur_char = passtrip[i]
        if passtrip[i+1] == cur_char and passtrip[i+2] == cur_char:
            triplets += 1

    subs = get_digit_substrings(password)
    feet = []
    res = []

    for i in subs:
        if has_consecutive_numbers(i):
            feet.append(i)

    for i in feet:
        res.append(find_longest_consecutive_substring(i))

    for i in res:
        steps += len(i) // 2

    if triplets != 0:
        steps += triplets

    if steps == 0:
        print("good!")
    else:
        print(steps)




if __name__ == '__main__':
    main()