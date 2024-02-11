import threading


def fun1(num, name):
    for i in range(num):
        print(f'Thread {name} : {i}')


if __name__ == "__main__":
    t1 = threading.Thread(target=fun1, args=(100, 'T1'))
    t2 = threading.Thread(target=fun1, args=(100, 'T2'))
    print(f"Total count : {threading.active_count()}")
    t1.start()
    t2.start()
    print(f"Total count : {threading.active_count()}")
    t1.join()
    t2.join()
    print(f"Total count : {threading.active_count()}")
    print("Done!")
