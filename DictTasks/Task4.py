"""Создайте словарь с количеством элементов не менее 5-ти.
Поменяйте местами первый и последний элемент объекта.
Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value».
Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
"""

dictionary = {
    1: 'мама',
    2: 'папа',
    3: 'деда',
    4: 'баба',
    5: 'брат'
}
addr = id(dictionary)

dictionary[1], dictionary[5] = dictionary[5], dictionary[1]
dictionary.pop(2)
dictionary['new_key'] = 'new_value'
print(dictionary)

print(id(dictionary) == addr)