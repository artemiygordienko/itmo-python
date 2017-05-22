# Функции

def say_hello():  # Только латинские буквы, на цифру начинаться нельзя
    print('Hello, python!')


say_hello()  # вызов функции


# Аргументы функции

def say_hello_2(name):
    print('Hello,', name)


say_hello_2('Вася')
say_hello_2('Петя')


def summa(a, b):
    print('Сумма:', a + b)


summa(1, 2)
summa('str1', 'str2')


# Как вернуть значение из функции?

def mega_pow(x, p):
    return x ** p


#
#
# def connect(host, user, passwd, dbname):
#     # if db_connect(host, user, passwd):
#     #     if db_set(dbname):
#     #         print('Работаем')
#     #     else:
#     #         print('Нет такой базы')
#     # else:
#     #     print('Нет соединения')
#     if not db_connect(host, user, passwd):
#         print('Нет соединения')
#         return False
#     if not db_set(dbname):
#         print('Нет такой БД!'):
#         return True

c = mega_pow(2, 8)
print(c)

print(mega_pow(3, 5))
mega_pow(mega_pow(5, 8), 2)


# Значение аргументов по умолчанию

def extra_pow(x, p=2):
    return x ** p


print('Extra pow:', extra_pow(2))
print('Extra pow:', extra_pow(2, 3))


def extra_pow(p, x=None):


# if x is None:
#     x = {}
#     x = x or {}
#     return x ** p


# Передача значений аргументов по ссылке

def parse(src, output):
    src = src.strip(".")  # Удалить символы с конца и начала строки strip
    for i in src.split():  # Разбивает строчку по символу разделителю(пробел, если не указано)
        output.append(i)


src = 'Python is a programming language.'
lst = []
parse(src, lst)
print(src, lst)


# Переменное количество аргументов
def multi(*args):
    result = initial
    for i in args:
        result *= i
    return result

lst2 = [1,2,3,4,5]
print(multi(*lst2)
print(multi(1, 2, 3))