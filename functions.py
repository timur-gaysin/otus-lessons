"""
1. Написать функцию, которая принимает неограниченное количество чисел в виде позиционных аргументов и ключевой
 аргумент — операцию над этими числами (сложение или умножение).Функция должна возвращать результат выполнения указанной операции.
"""

def calculate(*numbers, operation):
    if operation== "add":
        result = 0
        for n in numbers:
            result +=n
        return result   
    elif operation == "mul":
        result = 1
        for n in numbers:
            result *=n
        return result
    else:
        print("Неизвестная операция")
    

"""
2. Написать функцию для ввода из консоли целого числа.
Если введено не число, функция должна вывести соответствующее сообщение и предложить ввести значение заново — до тех пор, 
пока пользователь не введёт корректное число.
"""
def input_integer():
    while True:
        value  = input("Введите целое число: ")

        try:
            return int(value)
        except ValueError:
            print("Ошибка: нужно ввести целое число")


"""
3. Написать функцию, которая создаёт абсолютный путь к файлу.
Позиционные аргументы:
название диска,
неограниченное количество папок,
имя файла (без расширения).
Ключевые аргументы:
ext — расширение файла,
sep — разделитель (по умолчанию '/').
Пример:
full_path('c:', 'work', 'python', 'function', 'main', ext='py') ➜ 'c:/work/python/function/main.py'
"""

def full_path(disk, * folders, filename, ext, sep="/"):
    path_parts = [disk] + list(folders)
    path = sep.join(path_parts)
    return f"{path}{sep}{filename}.{ext}"



"""
4. Написать функцию, которая принимает список, состоящий из объектов разных типов, и возвращает словарь, где:
ключи — типы данных объектов;
значения — списки объектов соответствующего типа.
"""

def group_by_type(items):
    result = {}

    for item in items:
        item_type = type(item)

        if item_type not in result:
            result[item_type] = []

        result[item_type].append(item)

    return result



        


#Проверка первой задачи
print(calculate(1, 2, 3, 4, operation="add"))    
#Проверка второй задачи
input_integer()
#Проверка третье задачи
result = full_path('c:','Games','WarCraft III',filename='WarCraft III',ext='exe')
print(result)
#Проверка четвертой задачи
data = ["Текст", 's',1,4,4.5, True]
result= group_by_type(data)
for key, value in result.items():
    print(key, "->" , value)