def generate_combinations(variables, current_combination=[]):
    if len(current_combination) == len(variables):
        yield current_combination
    else:
        for value in [0, 1]:
            for combination in generate_combinations(variables, current_combination + [value]):
                yield combination

# Список переменных
variables = ['A', 'B', 'C']  # Замените этот список переменных на свой

# Создаем все комбинации из 0 и 1 для неопределенного количества переменных
combinations = list(generate_combinations(variables))

# Выводим комбинации
for combination in combinations:
    for i in range(len(variables)):
        print(f"{variables[i]} = {combination[i]}", end="  ")
    print()