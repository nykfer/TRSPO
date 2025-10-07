from multiprocessing import Pool
import time
import os

def theory(k:int) -> int:
    n = 0
    while k != 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = 3*k + 1
        n += 1
    return n


def main():
    numbers = range(1, 10_000_001)  # 1 млн чисел
    start = time.time()

    print(os.cpu_count())  # Використовуємо всі ядра
    # print(f"Запуск із {num_processes} процесами...")

    total_steps = 0
    processed = 0

    with Pool() as p:
        for steps in p.imap_unordered(theory, numbers, chunksize=1000):
            total_steps += steps
            processed += 1
            if processed % 100_000 == 0:
                print(f"Оброблено {processed:,} чисел...")

    mean = total_steps / len(numbers)
    finish = time.time()

    print(f"\nСередня кількість кроків: {mean:.2f}")
    print(f"Час виконання: {finish - start:.2f} с")


if __name__ == "__main__":
    main()
"""
Середня кількість кроків: 155.27
Час виконання: 66.87 с
"""