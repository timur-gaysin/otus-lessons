"""
1.Написать программу, которая получает на вход строку и возвращает словарь, где:
- ключи — символы из этой строки;
- значения — количество раз, сколько каждый символ встречается.
"""


text= input("Введите строку: ")

result = {}

for ch in text:
    if ch in result:
        result [ch] += 1
    else:
        result[ch] = 1

print(result);

"""
2. Дана строка текста (или введённая через консоль). Программа должна вернуть новую строку, в которой порядок слов будет обратным.
Пример:
"Python is really cool" → "cool really is Python".
"""

words = input("Введите строку: ").split()

reserver_words = words[::-1]
result = " ".join(reserver_words)

print(result)

"""
3. Написать программу, которая удаляет из списка все дубликаты, сохранив исходный порядок элементов.
"""

text = input("Введите элементы списка: ")

items = text.split()

result = []
duplicates = set()

for item in items:
    if item not in duplicates:
        result.append(item)
        duplicates.add(item)

print(result)

"""
4. Даны три (или больше) списка с объектами. Программа должна создать новый список, содержащий все уникальные элементы — каждый объект встречается только один раз.
"""
list1 = [1, 7, 2]
list2 = [3, 5, 4]
list3 = [9, 6, 7]

result = []
duplicates = set()

for lst in (list1,list2,list3):
    for item in lst:
        if item not in duplicates:
            result.append(item)
            duplicates.add(item)

print(result) 

"""
5. Дана строка текста (или введённая через консоль). Программа должна вернуть словарь с четырьмя ключами:
"гласные",

"согласные",

"цифры",

"пунктуация".

Значения — количество символов каждого типа в строке.
"""

text = input("Введите строку: ")

vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
consonants = "бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
punctuation = ".,!?;:-()[]{}\"'"


result = {
    "гласные": 0,
    "согласные": 0,
    "цифры": 0,
    "пунктуация": 0,
}

for ch in text:
    if ch in vowels:
        result["гласные"] +=1 
    elif ch in consonants:
        result["согласные"] += 1
    elif ch in punctuation:
        result["пунктуация"] +=1
    elif ch.isdigit():
        result["цифры"] += 1

print(result)