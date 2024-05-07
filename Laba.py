# Завдання 1
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить максимум у списку. Другий потік знаходить мінімум
# у списку. Результати обчислень виведіть на екран.
import threading

def find_max(list):
    maximum = max(list)
    print(f"Максимум у списку: {maximum}")

def find_minimum(list):
    minimum = min(list)
    print(f"Мінімум у списку: {minimum}")

entered_values = input("Введіть значення у список через пробіл: ").split()
list = [int(x) for x in entered_values]

p1 = threading.Thread(target=find_max, args=(list,))
p1.start()

p2 = threading.Thread(target=find_minimum, args=(list,))
p2.start()

p1.join()
p2.join()
