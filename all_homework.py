from module import *
from functools import reduce
import os

'''
Здесь только меню, все функции с домашних заданий с * и ** в module
'''
while True:
    os.system("cls")
    n = input('''
    Выберете:
    1.* Написать первую программу
    2.* Напишите скрипт решения квадратного уравнения
    3.* XOR шифрование
    4.* Частота использования цифр в диапазоне чисел
    5.* Частота использования символов в тексте
    6.* Удалить из списка элементы, значения которых уже встречались в этом же списке в предыдущих элементах
    7.* Вводится текст, содержащий различные скобки, необходимо определить, все ли скобки расставлены корректно
    8.* Вычисление факториала числа с использованием lambda
    9.* Написать программу подсчета частоты вхождений символов в текст с использованием lambda
    10.* Написать калькулятор для базовых операций сложения, вычитания, умножения, деления, возведения в степень
    11. ** FizzBuzz от 0 до 100, требуется наименьшая длина кода
    12. ** Решение квадратного уравнения с использованием комплексных чисел
    13. ** Алгоритм обхода дерева без использования рекурсии
    14. ** Вводится математический пример произвольной длины, необходимо решить пример
    15. ** Вычисление факториала числа с использованием lambda
    Пустой ввод - выход.
    ''')
    if n == '1':
        os.system("cls")
        first_prog()
        input('Для продолженя нажмите enter')
    if n == '2':
        os.system("cls")
        equation()
        input('Для продолженя нажмите enter')
    if n == '3':
        os.system("cls")
        try:
            str = input("Введите текст: ")
            if not str:
                str = read_from_file()
            key = int(input("Введите ключ: "))
        except:
            print('Еще раз')
            continue
        temp = xor(str, key)
        print(f'Зашифрованный/расшифрованный текст: {temp}')
        input('Для продолженя нажмите enter')
    if n == '4':
        os.system("cls")
        try:
            start = int(input("Введите начало диапазона: "))
            end = int(input("Введите конец диапазона: "))
        except:
            print('Еще раз')
            continue
        use_digits(start,end)
        input('Для продолженя нажмите enter')
    if n == '5':
        os.system("cls")
        stroka = input("Введите текст: ")
        if not stroka:
            stroka = read_from_file()
        stroka = str(stroka)
        use_alpha(stroka)
        input('Для продолженя нажмите enter')
    if n == '6':
        os.system("cls")
        _list = [i for i in input('Введите значения элементов массива через пробел ').split()]
        print(f'После удаления повторяющихся элементов получим получим: {delem(_list)}')
        input('Для продолженя нажмите enter')
    if n == '7':
        os.system("cls")
        str = input("Введите текст: ")
        if not str:
            str = read_from_file()
        check_brackets(str)
        input('Для продолженя нажмите enter')
    if n == '8':
        os.system("cls")
        while True:
            try:
                a = int(input('Введите число факториал которого хотите узнать: '))
            except:
                print('Еще раз!')
                continue
            if a < 0:
                print('Еще раз!')
                continue
            break
        print(f'Факториал {a} равен {reduce(lambda x,y:x*y,range(1,a+1))}')
        input('Для продолженя нажмите enter')
    if n == '9':
        os.system("cls")
        string = input("Введите текст: ")
        if not string:
            string = read_from_file()
        count = list(map(lambda x: {x: string.count(x)}, set(string)))
        for i in range(0,len(count)-1):
            print(count[i])
            input('Для продолженя нажмите enter')
    if n == '10':
        os.system("cls")
        calc()
    if n == '11':
        os.system("cls")
        for n in range(0, 101):
            fizzbuzz(n)
        input('Для продолженя нажмите enter')
    if n == '12':
        os.system("cls")
        equation()
        input('Для продолженя нажмите enter')
    if n == '13':
        os.system("cls")
        print('Центрированный обход: ',end='')
        inorder(root)
        print('\nПрямой обход: ',end='')
        preorder(root)
        input('Для продолженя нажмите enter')
    if n == '14':
        os.system("cls")
        try:
            calculation(input('Введите пример, в котором между каждыми символами пробел: '))
        except:
            print('Вы неверно ввели пример!')
        input('Для продолженя нажмите enter')
    if n == '15':
        os.system("cls")
        while True:
            try:
                a = int(input('Введите число для которого посчитать факториал: '))
            except:
                print('Еще раз!')
                continue
            if a < 0:
                print('Еще раз!')
                continue
            break
        print(f'Факториал {a} равен {fact(a)}')
        input('Для продолженя нажмите enter')
    if n == '':
        print('Goodbye!')
        break