from prettytable import PrettyTable

def main():
    variables = []

    exp = input("Enter your expression: ")
    for i in exp:
        if (i.isalpha()):
            if (i not in variables):
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
    for i in range((len(combinations))):
        row = []
        new_exp = updated_exp[:]
        for j in range(len(combinations[i])):
            row.append(combinations[i][j])
            new_exp = new_exp.replace(variables[j], str(combinations[i][j]))
        ex = eval(new_exp)
        if (ex in ["False", "0", 0]):
            row.append(0)
        elif (ex in ["True", "1", 1]):
            row.append(1)
        table.append(row)
    

    for i in range((len(combinations))):
        x.add_row(table[i])
    print(x)


def combs(variables, cur_comb = []):
    if (len(variables) == len(cur_comb)):
        yield cur_comb
    else:
        for v in ['0', '1']:
            for comb in combs(variables, cur_comb + [v]):
                yield comb

main()