# условный оператор

a = 50
b = 10

if a < b:
    print('a < b')        #pass-пустой блок кода
elif a == b:
    print('a = b')
else:                     #else-это зло и лучше избавляться
    print('a >= b')


# ТЕРНАРНЫЙ ОПЕРАТОР
uid = None

uid = uid if uid is not None else 1

print(1) if a < b else print(2)

#ЦИКЛЫ

i = 0
while True:             # пока, пока что-то
    if i % 2:
        print(i)
    if i > 10:
        break
    i += 1


#Цикл for

for i in [1, 2, 3, 4, 5]:
    print (i)

d = {
    'id': 1,
    'fio': 'Иван Иванович',
    'is_developer': True
}
for i in d.items():
    print(i)

a = 1
b = 2
b, a = a, b

#for key, value in d.items():
#print(key, value)
#for key in d.keys(): #перебирает ключи словаря
#    print(key)
for value in d.items(): #перебирает значения словаря
    print(value)

keys = ['id', 'fio', 'is_developer']
values = [2, 'Петр Петрович', False]

print (dict(zip(keys,values)))

for i in range(10, 20, 2):
    print (i)

# Сколько элементов в кортеже или списке?

print('Длина values:', len(values))

# Сколько повторяющихся элементов в кортеже или списке?

lst = [1, 2, 2, 2, 3, 1, 3]
print(lst.count(2))

# Получение части строки, списка

s1 = 'I love Python!'
print(s1[0], type(s1[0]))
print(s1[2:6])
print(s1[:6])
print(s1[7:])
print(s1[::2])
print(s1[2:6:2])
print(s1[-3:-1])
a = -5
print(s1[a:])
print(s1[::-1])

# Методы списков

lst1 = [1, 23, 4, 5, 6, 8, 8]
lst2 = lst1
lst2.append(666)        # Добавление элемента в конец
lst2.insert(0, 777)     # вставка в начало списка
lst2.remove(8)        # удаление элемента из списка
print(lst2.index(4))    # индекс элемента
del lst1                # удаление переменной
del lst2[2]             # удаление элемента списка
if 88 in lst2:
    lst2.remove(88)
if 'fio' in d:
    print(d['fio'])
skills = d['skills'] if 'skills' in d else []
d['skills'] = None
print (d.get('skills'))
print (d.get('skills,[1, 2]')) #со значением по умолчанию
skills = d.get('skills',[]) or []
print(skills)
