def print_params(a = 1, b = 'строка', c = True):
    print(f'a = {a},  b = {b},  c = {c}')


print('\nФункция с параметрами по умолчанию:')

print_params()
print_params('один')
print_params('один', 5)
print_params('один', 5, False)
print_params(c=100500, b={1, 2, 3})

print('\nРаспаковка параметров:')

values_list = [1, 'два', {1, 2, 3}]
values_dict = {'a': 100, 'b': True, 'c': '300'}
print_params(*values_list)
print_params(**values_dict)

print('\nРаспаковка + отдельные параметры:')

values_list_2 = [100500, False]
print_params(*values_list_2, 42)