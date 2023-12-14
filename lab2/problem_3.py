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

    if triplets != 0:
        steps += triplets

    if steps == 0:
        print("good!")
    else:
        print(steps)


if __name__ == '__main__':
    main()