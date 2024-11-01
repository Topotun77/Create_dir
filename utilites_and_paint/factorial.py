# Произвольное число параметров

def test(par1, par2='Второй параметр', *par3,
         par4=f'Четвертый именованный параметр', **par5):
    print(f'par1 = {par1}')
    print(f'par2 = {par2}')
    print('par3 = картеж из:', *par3)
    print(f'par4 = {par4}')
    print(f'par5 = {par5}')


test(1, 2,3,4,5, par6='Шестой именованный параметр',
     par7='Седьмой именованный параметр')

# Рекурсия

def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1)*n


n = int(input('\nВведите число для вычисления факториала: '))
print(f'{n}! = {factorial(n)}')
