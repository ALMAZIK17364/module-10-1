import threading
import time
from time import sleep

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count):
            file.write(f"Какое-то слово №{i}\n")
            sleep(0.1)
        print(f"Завершилась запись в файл {file_name}")

funcs_time_start = time.time()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
funcs_time_end = time.time()

print(f"Работа потоков: {int(funcs_time_end - funcs_time_start)} секунд")

threads_time_start = time.time()

thread5 = threading.Thread(target=write_words, args=(10, "example5.txt"))
thread6 = threading.Thread(target=write_words, args=(30, "example6.txt"))
thread7 = threading.Thread(target=write_words, args=(200, "example7.txt"))
thread8 = threading.Thread(target=write_words, args=(100, "example8.txt"))

thread5.start()
thread6.start()
thread7.start()
thread8.start()

thread5.join()
thread6.join()
thread7.join()
thread8.join()

threads_time_end = time.time()

print(f"Работа потоков: {int(threads_time_end - threads_time_start)} секунд")