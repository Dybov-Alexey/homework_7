#у меня установлен python3

#забыли поставить:
#def task()
#    return True
#task()
def task():
    return True
task()

#не сконвертировали str в int
#a = input()
#a+=1
a = int(input())
a+=1

#Обращение к необъявленной переменной
#t = 1
#def update_t():
#    if t == 1:
#        t = 2
#update_t()
#t = 1
def update_t(t):
    if t == 1:
        t = 2
update_t(t)

#Обращение к несуществующей переменной
#if f == 0:
#    f+=1
f = 0
if f == 0:
    f+=1

#Забыли написать вложенный код
#def task(f):
#
#task(f)
def task(f):
	f+=1
task(f)

#Используем табы и пробелы одновременно
#t = 1
#def update_t(t):
#    if t == 1:
#        t = 2
#         t = 3
#update_t(t)
t = 1
def update_t(t):
    if t == 1:
        t = 2
        t = 3
update_t(t)