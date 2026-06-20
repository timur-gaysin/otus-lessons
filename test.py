number = input ("Введите целое число: ")

while len(number) > 1:
    total = 0
    for ch in number:
        total += int(ch)
    number = str(total)

print("Результат: ",number)