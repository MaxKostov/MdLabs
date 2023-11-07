from prettytable import PrettyTable


def main():
    exp = input("Enter your expression: ")

    variables = set()
    for char in exp:
        if char.isalpha():
            variables.add(char)

    combinations = list(combs(variables))

    x = PrettyTable()
    x.field_names = list(variables) + [exp]
    table = []

    for combination in combinations:
        row = list(combination)
        variable_mapping = dict(zip(variables, combination))

        try:
            result = evaluate_expression(exp, variable_mapping)
            row.append(result)
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
        for v in [0, 1]:
            for comb in combs(variables, cur_comb + [v]):
                yield comb


def evaluate_expression(exp, variables):
    for var, val in variables.items():
        exp = exp.replace(var, str(val))
    return eval(exp)


main()
