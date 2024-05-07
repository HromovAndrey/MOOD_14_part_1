# Завдання 2
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знаходить суму елементів у списку. Другий потік знаходить
# середнє арифметичне у списку. Результати обчислень
# виведіть на екран.
import threading

def find_suny(list):
    suma = sum(list)
    print(f"Сума елементів у списку: {suma}")

def find_average(list):
    avarage = sum(list) / len(list)
    print(f"Середнє арифметичне у списку: {avarage}")


entered_values = input("Введіть значення у список через пробіл: ").split()
list = [int(x) for x in entered_values]

p1 = threading.Thread(target=find_suny, args=(list,))
p1.start()

p2 = threading.Thread(target=find_average, args=(list,))
p2.start()

p1.join()
p2.join()
