# Завдання 4
# Користувач вводить з клавіатури шлях до файлу та
# слово для пошуку. Після чого запускається потік для
# пошуку цього слова у файлі. Результат пошуку виведіть
# на екран.

import threading
def word_search(go_file, word):
    search = False
    with open(go_file, 'r') as file:
        for line in file:
            if word in line:
                search = True
                break

    if search:
        print(f"Слово '{word}' знайдено у файлі.")
    else:
        print(f"Слово '{word}' не знайдено у файлі.")

go_file = input("Введіть шлях до файлу: ")
word_search1 = input("Введіть слово для пошуку: ")

p = threading.Thread(target=word_search, args=(go_file, word_search1))
p.start()

p.join()
