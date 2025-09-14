import random
from math import pi
import threading
import time

COUNT = 1_000_000_00
THREADS = 4

"""Функція для обчислення числа пі"""
def calculate_pi(results:list, index:int, points:int):

    circle_points = 0

    for _ in range(points):
        
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)

        if x*x+y*y < 1:
            circle_points += 1
        
    pi_c = 4* circle_points / COUNT
    results[index] = pi_c

"""Функція для виклику потоків"""
def multi_threads():
    """
    threads - масив з потоками 
    results - масив з результатами з кожного потоку
    points -  кількість точок для одного потоку
    """
    threads = []
    results = [None]*THREADS 
    points = int(COUNT/THREADS)

    for index in range(THREADS):
        t = threading.Thread(target=calculate_pi, args=(results, index, points))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return sum(results)

s = time.time()
result = multi_threads()
f = time.time()

exec_t = f - s
print(pi)
print(f'result {result} with time {exec_t} с')

"""
Результат для (кількість точок 1_000_000_00):
1 потоку - 42.77 секунди
2 потоки - 91 
4 потоки - 91
"""
