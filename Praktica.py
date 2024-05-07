# import threading
# def print_cude(num):
#     #можна додати for i on range(5):
#     print("Cude:{}" .format(num * num *num))
#
# def print_sqare(num):
#          print("Square:{}" .format(num * num * num))
#
# t1 = threading.Thread(target=print_sqare, args=(10,))
# t2 = threading.Thread(target=print_cude,args=(10,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("Done!")


# import theading
#
# def print_cube(num):
#     #можна додати  for i in range(5)
#     print("Cube:{}" .format(num * num * num))
#
# def print_square(num):
#          print("Square:{}" .format(num * num))
#
# t1 = theading.Thead(target=print_square, args=(10,))
# t2 = theading.Thread(target=print_cube, args=(10,))
# t1.start()
# t2.start()
# t2.join()
# t1.join()
#
# print("Done!")
#
#
# import theading
# def print_numbers():
#     for i in range(5):
#         print(i)
#
# thead = theading.Thread(target=print_numbers)
# thead.start()
#
# import theading
# shared_resource = 0
# lock = theading.Lock()
# def increment():
#     global shared_resource
#     for _ in range(10000):
#         lock.acquire()
#         shared_resource += 1
#         lock.release()
#
# def decrement():
#     global shared_resource
#     for _ in range(10000):
#         lock.acquire()
#         shared_resource -= 1
#         lock.release()
#
# t1 = theading.Thread(target=increment)
# t2 = theading.Thread(target=decrement)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# print("Final value of shared resource:", shared_resource)

#
# import queue
# import threading
#
# task_queue = queue.Queue()
#
# def worker():
#     while True:
#         item = task_queue.get()
#         if item is None:
#             break
#         print ("Task:", item)
#         task_queue.task_done()
#
# threads = []
# for _ in range(4):
#     thread = threading.Thread(target=worker)
#     thread.start()
#     threads.append(thread)
# for item in range(10):
#     task_queue.put(item)
#
# for _ in range(4):
#     task_queue.put(None)
#
# for thread in threads:
#     thread.join()
#
#
# import multiprocessing
#
# def print_cude(num):
#     print("Cude:{}".format(num * num *num))
#
# def print_aquare(num):
#      """
#      fuction to print square of given num
#      :param num:
#      :return:
#      """
#      print("Square:{}".format(num * num))
#
# if __num__== "__main__":
#     #creting progresses
# p1 = multiprocessing.Process(target=print_aquare, args=(10,))
#
# p2 = multiprocessing.Process(target=print_aquare, args=(10,))
#
# #starting progress 1
# p1.start()
# #starting progress 2
# p2.start()
# #wait until process 1 is finished
# p1.join()
# #wait until process 2 is finished
# p2.join()
# #both progress finished
# print("Done!")



import threading
import random
 # Функція для обчисленн середнього значення у частині масиву

def calculate_mean(arr):
    mean = sum(arr) / len(arr)
    return mean

#Генеруємо великий масив данних
data_size = 10000 # Розмир масиву
data = [random.randint(0, 1000) for _ in rsange(data_size)]

#кількість потоків для паралельної обробки
num_threads = 4 #Можна вірювати кількість потоків
#Розділяємо масив на частини для обробки кожним потоком
chunk_size = len(data) // num_threads
chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

# Зберігаємо результати обчислень у потоках
results = []
#Створення та запуск потоків для обчислення середнього значення
threads = []
for chunk in chunks:
    thread = threading.Thread(target=Lambda x:results.append(calculate_mean(x)), args=(chunk,))
    threads.append(thread)
    thread.start()

#Чекаємо завершення кожного потоку
for thread in threads:
    thread.join()

#Обчислюємо загальне середнє значення
total_men = sum(results) / len(results)

print(f"Середнє значення у великому масиві:{total_men}")

import tkinter as tk
import threading
import time

def start_computation():
    #Функція для виконання обчислень
    for i in range(1, 11):
        time.sleep(1) # Імітація обчислень(чукаємо 1 секунду)
        label["text"] = f"Обчислення: {i}"
# Обчислення тексту у віджеті Label
def start_thread():
    #Функція для старту потку для обчислень
thread = threading.Thread(target=start_computation)
thread.start()
#Створення вікна TKinter
root = tk.Tk()
root.title("Графічний інтерфейс с потоками")
#Створення віджетів
label = tk.Label(root, text="Натисніть кнопку для початку обчислень")
label.pack(pady=20)
button = tk.Button(root, text="Почати обчислення", command=start_thread)
button.pack(pady=10)
#Запуск головного циклу Tkinter
root.mainloop()




import os
import multiprocessing
#Функція для обробки кожного файлу
def process_file(file):
    #Тут можна реалізува ти логіку обролбки/ перевірки файлу

#Наприклад можна прочитати вмыст файлу та провести операцыъ над ним
with open(file, "r") as file:
    file_content = f.read()
    #Приклад перевірки  наявності певної інформіції у файлі
    if "шуканий_текс" in file_content:
        print(f"Файл{file}:знайдено шукану інформацію")
    else:
        print(f"Файл:{file}:укана інформація не знайдена")

if __name__=="__main__":
#Перелік файлів   які треба обробити (можна змінити на свій)
    file_to_process = ["file.txt", "file2.txt", "file3.txt"]

#Створення пулу прцесів для паралельної обробки файдів
with multiprocessing.Pool() as pool:
    #Запуск файлів proxess_file для кожного файлу
pool.map(process_file, file_to_process)