def xor(stroka,key):
    """XOR шифрование
    На вход строка и ключ
    Возвращает зашифрованное XORом сообщение
    """
    s = ""
    for symbol in stroka:
        s += chr(ord(symbol)^key)
    return s


def usedigits(start,end):
    """Частота использования цифр в диапазоне чисел
    На вход начало и конец диапазона
    Ничего не возвращает
    """
    st = ''
    for s in range(start,end+1):
        st += str(s)
    print(f'Записываем значения в одну строку: {st}')
    for i in range (0,10):
        print(f"Число {i} встречается {st.count(str(i))} раз(a)")


def usealpha(stroka):
    """Частота использования символов в тексте
    На вход строка
    Ничего не возвращает
    """
    stroka = str(stroka)
    print(f'Введенная строка: {stroka}')
    while len(stroka) != 0:
        print(f'Символ {stroka[0]} встречается {stroka.count(stroka[0])} раз(а)')
        stroka = stroka.replace(stroka[0],'')


while 1:
    print('Выберите задачу:')
    print('1. XOR шифрование.')
    print('2. Частота использования цифр в диапазоне чисел.')
    print('3. Частота использования символов в тексте.')
    print('4. Выход.')
    a = int(input())
    if a == 1:
        k,key = input("Введите зашифрованную или расшфрованную строку и ключ через пробел ").split()
        if key.isdigit():
            key = int(key)
            print(f'Зашифрованное/расшифрованное слово: {xor(k,key)}')
        else:
            print('Введен неверный символ')
    elif a == 2:
        x, y = input("Введите диапазон чисел через пробел(от х до у) ").split()
        x = int(x)
        y = int(y)
        usedigits(x,y)
    elif a == 3:
            x = str(input("Введите строку "))
            usealpha(x)
    elif a == 4:
        print('Goodbye!')
        break
    else:
        print('Введен неверный символ')