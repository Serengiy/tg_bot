import json
import string

lst = json.load(open('mat.json'))

# s = 'Это предложение без мата'
# f = 'Это пиздец предложение с матом'

# print(set(json.load(open('mat.json'))))
# print({i.lower().translate(str.maketrans('', '', string.punctuation)) for i in s.split(' ')}.intersection(set(json.load(open('mat.json')))))


# s_upd = {'Это', 'предложение', 'без', 'мата'}
# f_upd = {'Это', 'пиздец', 'без', 'мата'}

# print(lst)
# print(s_upd.intersection(lst))
# words = ['a', 'a', 'b', 'b', 'c', 'd', 'e']
# mySet = set(words)
#
# print(str(mySet))


menu = {'/Напитки': 'drinks', '/Горячее': 'hots', "/Салаты": 'salads'}
print(tuple(menu.values())[1::])

