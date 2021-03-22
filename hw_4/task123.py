def bubble(arr):
    """Cортровка пузырьком
    На вход массив
    Возвращает отсортированный массив"""
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
a = [4,3,5,2,1]


def compare_list(list1,list2):
    """Даны два списка, совпадают ли множества их элементов
    На вход 2 списка
    Возвращает True/False"""
    """# Можно просто сравнивать списки, 
    # if list1 == list2:
    #     return True
    # else:
    #     return False"""
    for i in range(min(len(list2),len(list1))):
        if list1[i] != list2[i]:
            return False
    return True


while True:
    n = input(
"""
Выберите задачу.
1. Пузырек.
2. Даны два списка. Определите, совпадают ли множества их элементов.
3. Выполнял в пред. дз
Выход:                                              Enter
"""
    )
    if n == "1":
        _list = [int(i) for i in input('Введите значения элементов массива через пробел ').split()]
        print(f'После сотировки пузырьковым методом получим: {bubble(_list)}')
    elif n == "2":
        listset1 = []
        listset2 = []
        print('Инструкция:\nВы сначала вы вводите значения элементов множества первого списка через enter\nКогда вы больше не хотите вводить, нажимаете enter с пустыми значениями множества')
        while True:
            _list = [int(i) for i in input('Введите значения элементов множества через пробел, если хотите выйти, enter в пустом множестве ').split()]
            if not _list:
                break
            else:
                set1 = set(_list)
                listset1.append(set1)
        print(f'Первый список - {listset1}')
        print('Для второго списка аналогично')
        while True:
            _list = [int(i) for i in input('Введите значения элементов множества через пробел, если хотите выйти, enter в пустом множестве ').split()]
            if not _list:
                break
            else:
                set1 = set(_list)
                listset2.append(set1)
        print(f'Второй список список - {listset1}')
        print(f'Определите, совпадают ли множества их элементов - {compare_list(listset1,listset2)}')
    elif not n:
        print("Goodbye!")
        break
    else:
        print("Неверный символ")