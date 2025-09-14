import random
from math import pi
import multiprocessing
import time

COUNT = 1_000_000_00
PROCESSES = 32

def calculate_pi(results:list, index:int, points:int):

    circle_points = 0

    for _ in range(points):
        
        x = random.uniform(-1.0, 1.0)
        y = random.uniform(-1.0, 1.0)

        if x*x+y*y < 1:
            circle_points += 1
        
    pi_c = 4* circle_points / COUNT
    results[index] = pi_c

def multi_processes():
    with multiprocessing.Manager() as manager:
        results = manager.list([None] * PROCESSES)  # shared list
        processes = []
        points = int(COUNT / PROCESSES)

        for index in range(PROCESSES):
            p = multiprocessing.Process(target=calculate_pi, args=(results, index, points))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

        return sum(results) 

s = time.time()
result = multi_processes()
f = time.time()

exec_t = f - s
print(pi)
print(f'result {result} with time {exec_t} с')

"""
Результат для (кількість точок 1_000_000_00):
1 процес - 53.22 секунди
2 процеси - 21.8 
4 процеси- 13
8 процесів - 11
16 процесів - 11
32 процеси - 11.5
"""