from multiprocessing import Pool, Manager
import time
import random
import os

def theory(k:int):
    pid = os.getpid()
    if pid not in pids:
        pids.append(pid)
    n = 0

    while(k != 1):
        if k % 2 == 0:
            k //= 2
        else:
            k = 3*k + 1
        n += 1
    
    return n

numbers = [random.randint(2, 1000) for x in range(1_00_000)]
# print(numbers)
# print("==================================================")
start = time.time()
with Manager() as manager:

    pids = manager.list()

    with Pool() as p:
        result = p.map(theory, numbers, chunksize=1)
        print(f'Кількість процесів - {p._processes}')
        print('=============================================')
    
    print(f'Задіянна кількість процесів - {len(pids)}')
finish = time.time()

mean = sum(result)/len(result)
print(f"Середня кількість кроків - {mean}")
print(f"Час виконання завдання - {finish - start}")

# print(theory(845))