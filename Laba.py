# Завдання 3
# Користувач вводить з клавіатури шлях до файлу, що
# містить набір чисел. Після чого запускаються два потоки.
# Перший потік створює новий файл, в який запише лише
# парні елементи списку. Другий потік створює новий файл,
# в який запише лише непарні елементи списку. Кількість
# парних і непарних елементів виводиться на екран.

import threading
def even_numbers(path_file):
    couples = []
    with open(path_file, 'r') as file:
        numbres = [int(number) for number in file.read().split()]
        couples = [number for number in numbres if number % 2 == 0]

    with open('парні_числа.txt', 'w') as new_file:
        for number in couples:
            new_file.write(str(number) + '\n')

    print(f"Кількість парних чисел: {len(couples)}")

def odd_numbers(path_file):
    odd = []
    with open(path_file, 'r') as file:
        numbers = [int(number) for number in file.read().split()]
        odd = [number for number in numbers if number % 2 != 0]

    with open('непарні_числа.txt', 'w') as new_file:
        for number in odd:
            new_file.write(str(number) + '\n')

    print(f"Кількість непарних чисел: {len(odd)}")
go_file = input("Введіть шлях до файлу з числами: ")

p1 = threading.Thread(target=even_numbers, args=(go_file,))
p1.start()

p2 = threading.Thread(target=odd_numbers, args=(go_file,))
p2.start()

p1.join()
p2.join()
