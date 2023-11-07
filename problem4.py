from prettytable import PrettyTable


def main():
    variables = []

    exp = input("Enter your expression: ")
    for i in exp:
        if i.isalpha():
            if i not in variables:
                variables.append(i)

    combinations = list(combs(variables))

    variables.append(exp)

    updated_exp = ""
    for c in exp:
        if c == '+':
            updated_exp += "or"
        elif c == '*':
            updated_exp += "and"
        elif c == '!':
            updated_exp += "not "
        else:
            updated_exp += c

    x = PrettyTable()
    x.field_names = variables
    table = []

    for combination in combinations:
        row = list(combination)
        variable_mapping = dict(zip(variables, combination))

        try:
            ex = eval(updated_exp, variable_mapping)
            if ex in [False, 0]:
                row.append(0)
            elif ex in [True, 1]:
                row.append(1)
            else:
                row.append(ex)
        except Exception as e:
            row.append("Error")

        table.append(row)

    for i in range(len(combinations)):
        x.add_row(table[i])

    print(x)


def combs(variables, cur_comb=[]):
    if len(variables) == len(cur_comb):
        yield cur_comb
    else:
        for v in ['0', '1']:
            for comb in combs(variables, cur_comb + [v]):
                yield comb


main()
