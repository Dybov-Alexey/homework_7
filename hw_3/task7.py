import math
import cmath
from os import fdopen


def diskriminant(a,b,c):
    return b*b-4*a*c


print('Выберите: \n 1. Если у вас коэффиценты не комплексные числа.\n 2. Если у вас коэффиценты комплексные числа.')
check = input()
if check.isdigit() and int(check) == 1:
    a = int(input("Введите коэффицент A: " ))
    b = int(input("Введите коэффицент B: " ))
    c = int(input("Введите коэффицент C: " ))
    print("Уравнение: (",a,")x^2 + (",b,")x + (",c,") = 0")
    if a == 0 and b !=0:
        x = -c / b
        if x == 0:
            print('Бесконечное множество корней')
        else:
            print('Один корень: ',x)
    elif b == 0 and a == 0 and c == 0:
        print('Бесконечное множество корней')
    elif b == 0 and a == 0 and c != 0:
        print(c," != 0")
        print('Некорректные данные')
    else:
        d = diskriminant(a,b,c)
        if d < 0:
            print('Дискриминант < 0, поэтому возможны только комплесные корни: ',end='')
            x = complex(math.sqrt(-d), 1)
            print(f'{-b/2*a} +/- {x/2*a}')
        elif d == 0:
            x = -1*b/2/a
            print('Один корень: ',x)
        else:
            x1 = (-1*b+math.sqrt(d))/2/a
            x2 = (-1*b-math.sqrt(d))/2/a
            print('Два корня: ',x1,x2)
elif check.isdigit() and int(check) == 2:
    print('Введите коэффицент А:')
    a1, a2 = input('Введите действительную часть и коэффицент перед мнимой частью через пробел: ').split()
    print('Введите коэффицент B:')
    b1, b2 = input('Введите действительную часть и коэффицент перед мнимой частью через пробел: ').split()
    print('Введите коэффицент C:')
    c1, c2 = input('Введите действительную часть и коэффицент перед мнимой частью через пробел: ').split()
    A = complex(int(a1),int(a2))
    B = complex(int(b1),int(b2))
    C = complex(int(c1),int(c2))
    print(f'Уравнение: {A}x^2 + {B}x + {C} = 0')
    x1 = (-1*B+cmath.sqrt(diskriminant(A,B,C)))/2/A
    x2 = (-1*B-cmath.sqrt(diskriminant(A,B,C)))/2/A
    print(f'Два комплексных корня: {x1}  {x2}')
else:
    print('Введен неверный символ') 