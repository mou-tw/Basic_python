import threading

def func1():
    for i in range(100):
        print(i , end= ', ')

def func2(n):
    for i in range(n):
        print('f2',i, end=', ')


threading.Thread(target=func1).start()
threading.Thread(target=func2(5)).start()

# threading.Thread(target=func1).join()
# threading.Thread(target=func2).join()

