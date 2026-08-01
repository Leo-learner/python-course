import time
import functools
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} 耗时：{end - start:.6f}")
        return result
    return wrapper

@timer 
def add(a, b):
    return a + b

@timer 
def slow():
    time.sleep(1)
    return "done"

print(add(3, 4))
print(slow())

print(add.__name__)  # 输出 add
