def test():
    a = 1
    b = 'два'
    global d
    d *= 5
    print(f'Внутри test:        a = {a}, b = {b}, c = {c}, d = {d}')


def test2(par_1=1, par_2=2, par_3=3):
    print(f'par_1 = {par_1}', f'par_2 = {par_2}', f'par_3 = {par_3}', sep='\t\t', end='\n')

a, b = True, False
c = 100500
d = 46
print(f'До вызова test:     a = {a}, b = {b}, c = {c}, d = {d}')
test()
print(f'После вызова test:  a = {a}, b = {b}, c = {c}, d = {d}\n')
test2()
test2('10', 'два')
test2(par_3=77, par_2='два')
