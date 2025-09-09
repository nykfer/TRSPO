import threading
import multiprocessing

s = 0

def task1():
    s = 0
    for i in range(15):
        s+=i
    print(s)

def task2():
    s = 1
    for i in range(1, 15):
        s *= i* 100

    print(s)

def threads():
    print("Launched the threads\n")
    thread1 = threading.Thread(target=task1)
    thread2 = threading.Thread(target=task2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

def processes():
    print("Launched the processes\n")
    process1 = multiprocessing.Process(target=task1)
    process2 = multiprocessing.Process(target=task2)

    process1.start()
    process2.start()

    process1.join()
    process2.join()

if __name__ == '__main__':
    threads()
    processes()