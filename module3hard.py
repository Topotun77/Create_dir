data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_):
    sum = 0
    for x in data_:
        if isinstance(x, set) or isinstance(x, list) or isinstance(x, tuple):
            sum += calculate_structure_sum(x)
        elif isinstance(x, dict):
            sum += calculate_structure_sum(x) + calculate_structure_sum(list(x.values()))
        elif isinstance(x, int) or isinstance(x, float):
            sum += x
        elif isinstance(x, str):
            sum += len(x)
        else:
            print(f'Не могу понять, что это за тип данных {x}')

    return sum


result = calculate_structure_sum(data_structure)
print(result)