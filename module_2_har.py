print('испытание началось')

import random

n = random.randint(3, 20)


def old_shifr(n):
    result = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                result += str(i) + str(j)
    return result


shifr = old_shifr(n)
print(f'Число первой вставки {n}')
print(f'число второй вставки" {shifr}')
print('Congratulations, mission accomplished')

