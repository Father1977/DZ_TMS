from time import time
def timemometr(func):

    def wrapper(*args):
        start_time = time()
        value = func(*args)
        end_time = time()
        print(f'Время выполнения функции {end_time-start_time} сек.')
        return value
    return wrapper
@timemometr
def summa(a, b):
    from time import sleep
    sleep(2)
    return a + b
print(summa(4,5))