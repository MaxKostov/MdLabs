from prettytable import PrettyTable

try:
    expression = input("Expression: ")
    expression = ' '.join(expression)

    variables = set([char for char in expression if char.isalpha()])
    variables = list(variables)
    num_variables = len(variables)


    header = variables + [expression]


    table = PrettyTable(header)


    for i in range(2 ** num_variables):
        variable_values = [bool((i >> j) & 1) for j in range(num_variables)]
        variable_dict = dict(zip(variables, variable_values))


        modified_expression = expression.replace('! ', 'not ').replace('* ', 'and ').replace('+ ', 'or ')
        result = eval(modified_expression, variable_dict)
        row = variable_values + [result]
        table.add_row(row)

    print(table)
except SyntaxError:
    print("Incorrect input")